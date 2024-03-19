import numpy as np
import cv2 as cv

normal = cv.imread('../_img/tony-img.jpg')
smile = cv.imread('../_img/tony2-img.jpg')

img = cv.add(normal, smile)
cv.imshow('addition', img)

cv.waitKey(0)
cv.destroyAllWindows()