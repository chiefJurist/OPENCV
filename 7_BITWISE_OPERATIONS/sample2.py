import numpy as np
import cv2 as cv

img1 = cv.imread("../_img/img-a.png")
img2 = cv.imread("../_img/logo.png")

rows, cols, channels = img2.shape

roi = img1[0:rows, 0:cols]

img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)

mask_inv = cv.bitwise_not(mask)

#Now black out the area of the logo
img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)

#Take only region of logo from logo image
img2_fg = cv.bitwise_and(img2,img2, mask= mask)

#Put logo in ROI
dst = cv.add(img2_fg, img1_bg)
img1[0:rows, 0:cols] = dst

cv.imshow("Result", img1)
cv.waitKey(0)
cv.destroyAllWindows()