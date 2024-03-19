import numpy as np
import cv2 as cv

img = cv.imread('../_img/home.png')
cv.imshow("Original", img)

gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
sift = cv.SIFT_create()
kp = sift.detect(gray,None)
img=cv.drawKeypoints(gray,kp,img)
cv.imwrite('../_img/keypoints.jpg',img)

cv.imshow("Keypoints", img)
cv.waitKey(0)
cv.destroyAllWindows()