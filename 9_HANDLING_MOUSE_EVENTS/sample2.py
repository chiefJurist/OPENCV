import numpy as np
import cv2 as cv

drawing = True
shape = "r"

#mouse callback function
def drawCircle(event,x,y,flags,param):
    global x1, x2
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        x1, x2 = x, y
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if shape == 'r':
            cv.rectangle(img,(x1,x2),(x,y),(0,255,0),-1)
        if shape == 'l':
            cv.line(img,(x1,x2),(x,y),(255,255,255),3)
        if shape=='c':
            cv.circle(img,(x,y), 10, (255,255,0), -1)

img = cv.imread('../_img/img-b.png')
cv.namedWindow('image')
cv.setMouseCallback('image',drawCircle)

while(1):
    cv.imshow('image',img)
    key=cv.waitKey(1)
    if key==ord('1'):
        shape='r'
    if key==ord('2'):
        shape='l'
    if key==ord('3'):
        shape='c'
 #print (shape)
    if key == 27:
        break
cv.destroyAllWindows()        