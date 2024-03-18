import numpy as np
import cv2 as cv

img = cv.imread("../_img/img-a.png")
text = "My Baby Girl"
font = cv.FONT_HERSHEY_SIMPLEX

cv.putText(img, text, (10,100), font, 2, (255,255,255) , 2, cv.LINE_AA)

cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()