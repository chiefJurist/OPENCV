import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("../_img/img-b.png", 1)

print(img.shape)

# In the above command:
#  The first two items shape[0] and shape[1] represent height and width of the image. 
#  Shape[2] stands for a number of channels. 
#  3 indicates that the image has Red Green Blue (RGB) channels.

# The shape() method of this ndarray 
# object reveals image properties such as dimensions and channels. 