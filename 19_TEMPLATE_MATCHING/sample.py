import cv2 as cv
import numpy as np

img = cv.imread('../_img/Dhoni-and-Virat.png',1)
cv.imshow('Original',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

template = cv.imread('../_img/Virat.png',0)
cv.imshow('Template',template)

w,h = template.shape[0], template.shape[1]

matched = cv.matchTemplate(gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( matched >= threshold)
for pt in zip(*loc[::-1]):
    matchedImg = cv.rectangle(img, (pt[0], pt[0]), (pt[0] + w, pt[1] + h), (0,255,255), 2)
cv.imshow('Matched with Template',img)

cv.waitKey(0)
cv.destroyAllWindows()