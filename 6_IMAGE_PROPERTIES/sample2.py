import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("../_img/img-b.png", 1)

#command for the size of an image 
print(img.size)

#Each element in the ndarray represents one image pixel. 