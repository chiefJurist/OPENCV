import cv2 as cv
import numpy as np

img = cv.imread('../_img/Linux-logo.png',0)

kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(img,kernel,iterations = 1)
dilation = cv.dilate(img,kernel,iterations = 1)

cv.imshow('Original', img)
cv.imshow('Erosion', erosion)
cv.imshow('Dialation', dilation)

cv.waitKey(0)
cv.destroyAllWindows()