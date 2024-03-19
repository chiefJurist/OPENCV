import numpy as np
import cv2 as cv

img = cv.imread('../_img/logo.png',1)

h, w = img.shape[:2]

center = (w / 2, h / 2)
mat = cv.getRotationMatrix2D(center, 90, 1)
rotimg = cv.warpAffine(img, mat, (h, w))

cv.imshow('original',img)
cv.imshow('rotated', rotimg)
cv.waitKey(0)
cv.destroyAllWindows()