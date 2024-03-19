import cv2 as cv

img = cv.imread('../_img/img-a.png')
img1 = cv.cvtColor(img, cv.COLOR_BGR2GRAY )
img2 = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Displaying the image
cv.imshow('original', img)
cv.imshow('Gray', img1)
cv.imshow('HSV', img2)

cv.waitKey(0)
cv.destroyAllWindows()