import numpy as np
import cv2

img1 = cv2.imread("../_img/image-a.png")
img2 = cv2.imread("../_img/image-b.png")

dest1 = cv2.bitwise_and(img1, img2, mask=None)
dest2 = cv2.bitwise_or(img1, img2, mask=None)
dest3 = cv2.bitwise_xor(img1, img2, mask=None)

cv2.imshow("A", img1)
cv2.imshow("B", img2)
cv2.imshow("AND", dest1)
cv2.imshow("OR", dest2)
cv2.imshow("XOR", dest3)
cv2.imshow("NOT A", cv2.bitwise_not(img1))
cv2.imshow("NOT B", cv2.bitwise_not(img2))

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()