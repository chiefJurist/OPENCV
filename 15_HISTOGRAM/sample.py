import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('../_img/img-a.png')
color = ('b','g','r')

for i,col in enumerate(color):
    hist = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])

plt.show()