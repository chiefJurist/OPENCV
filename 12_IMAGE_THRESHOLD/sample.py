import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('../_img/gradient.png',0)

ret,img1 = cv.threshold(img,127,255,cv.THRESH_BINARY)

plt.subplot(2,3,1),plt.imshow(img,'gray',vmin=0,vmax=255)
plt.title('Original')

plt.subplot(2,3,2),plt.imshow(img1,'gray',vmin=0,vmax=255)
plt.title('Binary')

plt.show()