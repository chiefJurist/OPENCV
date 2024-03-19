import numpy as np
import cv2 as cv

normal = cv.imread('../_img/tony-img.jpg')
smile = cv.imread('../_img/tony2-img.jpg')

img = cv.addWeighted(normal, 0.3, smile, 0.7, 0)
cv.imshow('addition', img)

cv.waitKey(0)
cv.destroyAllWindows()