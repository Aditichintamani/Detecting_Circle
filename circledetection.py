import cv2
import numpy as np

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
        #cv2.imshow("preview", frame)
        cv2.waitKey(1)
        rval, frame = vc.read()
        img = cv2.medianBlur(frame,5)
        imgg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        cimg = cv2.cvtColor(imgg,cv2.COLOR_GRAY2BGR)

        #circles = cv.HoughCircles(imgg, cv.HOUGH_GRADIENT, 1, 10, np.array([]), 100, 30, 1, 30)
        circles = cv2.HoughCircles(imgg,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=5,maxRadius=20)
        

        if circles is not None: # Check if circles have been found and only then iterate over these and add them to the image
            a, b, c = circles.shape

        
        if circles is None:
            cv2.imshow("preview", frame)
            continue
                
        print (circles)
        circles = np.uint16(np.around(circles))
        for i in range(b):
            cv2.circle(cimg, (circles[0][i][0], circles[0][i][1]), circles[0][i][2], (0, 0, 255), 3, cv2.LINE_AA)
            cv2.circle(cimg, (circles[0][i][0], circles[0][i][1]), 2, (0, 255, 0), 3, cv2.LINE_AA)  # draw center of circle
            
            for i in circles[0,:]:
                print(i)
                cv2.circle(cimg,(i[0],i[1]),i[2],(0,0,255),2, cv2.LINE_AA) # draw the outer circle
                cv2.circle(cimg,(i[0],i[1]),2,(0,255,0),3, cv2.LINE_AA)
            cv2.imshow("preview", frame)
            cv2.imshow("detected circles", cimg)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        #key = cv2.waitKey(20)
        #if key == 27:
                break
cv2.destroyWindow("preview")
