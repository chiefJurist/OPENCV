import numpy as np
import cv2 as cv

img1 = cv.imread('../_img/img-a.png')
img2 = cv.imread('../_img/naza-test.png')

# Convert it to grayscale
img1_bw = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
img2_bw = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

orb = cv.ORB_create()

queryKeypoints, queryDescriptors = orb.detectAndCompute(img1_bw,None)
trainKeypoints, trainDescriptors = orb.detectAndCompute(img2_bw,None)

matcher = cv.BFMatcher()
matches = matcher.match(queryDescriptors,trainDescriptors)

img = cv.drawMatches(img1, queryKeypoints,
img2, trainKeypoints, matches[:20],None)

img = cv.resize(img, (1000,650))

cv.imshow("Feature Match", img)
cv.waitKey(0)
cv.destroyAllWindows()
