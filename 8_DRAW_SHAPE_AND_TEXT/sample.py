import numpy as np
import cv2 as cv

img = cv.imread("../_img/img-a.png", 1)

cv.line(img, (20,400), (400,20), (255,255,255), 3)
cv.rectangle(img, (200,100), (400,400), (0,255,0), 5)
cv.circle(img, (80,80), 55, (255,255,0), -1)
cv.ellipse(img, (300,425), (80,20), 5, 0, 360, (0,0,255), -1)

cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()