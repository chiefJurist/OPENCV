import sys
import cv2 as cv

filename = '../_img/img-a.png'
src = cv.imread(filename)

while 1:
    print ("press 'i' for zoom in 'o' for zoom out esc to stop")

    rows, cols, channels = map(int, src.shape)
    cv.imshow('Pyramids', src)

    k = cv.waitKey(0)
    if k == 27:
        break

    elif chr(k) == 'i':
        src = cv.pyrUp(src, dstsize=(2 * cols, 2 * rows))

    elif chr(k) == 'o':
        src = cv.pyrDown(src, dstsize=(cols // 2, rows // 2))

cv.destroyAllWindows()
