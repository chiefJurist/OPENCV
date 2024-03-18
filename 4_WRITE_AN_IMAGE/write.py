import numpy as np
import cv2

#Load A Color Image In Grayscale
img = cv2.imread("../_img/img-c.png", 0)

cv2.imshow("image", img)
key = cv2.waitKey(0)

if key==ord("s") :
    #if an image exists with this file name, it will overwrite the image
    cv2.imwrite("../_img/img-write.png", img)

cv2.destroyAllWindows()