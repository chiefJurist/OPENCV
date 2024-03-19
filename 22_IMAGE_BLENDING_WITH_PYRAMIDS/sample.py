import cv2 as cv
import numpy as np,sys

normal = cv.imread('../_img/tony-img.jpg')
smile = cv.imread('../_img/tony2-img.jpg')

### generate Gaussian pyramid for first
G = normal.copy()
gpk = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpk.append(G)

# generate Gaussian pyramid for second
G = smile.copy()
gpe = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpe.append(G)

# generate Laplacian Pyramid for first
lpk = [gpk[5]]
for i in range(5,0,-1):
    GE = cv.pyrUp(gpk[i])
    L = cv.subtract(gpk[i-1],GE)
    lpk.append(L)

# generate Laplacian Pyramid for second
lpe = [gpe[5]]
for i in range(5,0,-1):
    GE = cv.pyrUp(gpe[i])
    L = cv.subtract(gpe[i-1],GE)
    lpe.append(L)

# Now add left and right halves of images in each level
LS = []
for la,lb in zip(lpk,lpe):
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:int(cols/2)], lb[:,int(cols/2):]))
    LS.append(ls)

    ls_ = LS[0]
for i in range(1,6):
    ls_ = cv.pyrUp(ls_)
    ls_ = cv.add(ls_, LS[i])
    cv.imshow('RESULT',ls_)

cv.waitKey(0)
cv.destroyAllWindows()
