import numpy as np
import cv2 as cv

#mouse callback function
def drawFunction(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), 20, (255,255,255), -1)

img = cv.imread("../_img/img-b.png")

cv.namedWindow("image")
cv.setMouseCallback("image", drawFunction)

while(1):
    cv.imshow("image", img)
    key = cv.waitKey(1)
    if key == 27:
        break

cv.destroyAllWindows()