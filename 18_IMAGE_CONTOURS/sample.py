# Before finding contours, we should apply threshold or canny edge detection. Then, by
# using findContours() method, we can find the contours in the binary image.
# After detecting the contour vectors, contours are drawn over the original image by using
# the cv.drawContours() function.

import cv2 as cv
import numpy as np

img = cv.imread('../_img/shapes.png')
cv.imshow('Original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny = cv.Canny(gray, 30, 200)

contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
print("Number of Contours = " ,len(contours))
cv.imshow('Canny Edges', canny)

cv.drawContours(img, contours, -1, (0, 255, 0), 3)
cv.imshow('Contours', img)

cv.waitKey(0)
cv.destroyAllWindows()