import numpy as np
import cv2 as cv

img = cv.imread('../_img/img-c.png',1)
height, width = img.shape[:2]
res = cv.resize(img,(int(width/2), int(height/2)), interpolation = cv.INTER_AREA)

cv.imshow("Main Image", img)
cv.imshow("Image", res)
cv.waitKey(0)
cv.destroyAllWindows()