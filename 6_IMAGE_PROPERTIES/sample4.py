import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("../_img/img-d.png", 1)

# split the image channels
# This line splits the loaded image img into its three color channels: blue (b), green (g),
# and red (r). Each channel is stored as a separate NumPy array. After this line executes, 
# b contains the blue channel of the image, g contains the green channel, and r contains the red channel.
b,g,r = cv2.split(img)

# You can now perform manipulation on each plane. 
# Suppose we set all pixels in blue channel to 0, the code will be as follows:
# This line modifies the blue channel of the image (img[:, :, 0]) by setting all pixel values in the blue channel to 0. 
# The syntax img[:, :, 0] means selecting all rows (:) and all columns (:) of the blue channel (index 0).
img[:, :, 0]=0


cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# So, effectively, this line sets the intensity of the blue color to 0 for all pixels in the image, 
# effectively removing the blue color from the image. This operation will result in the image 
# appearing with a different color balance or hue compared to the original. For example, if you remove the blue channel, 
# the image may appear more reddish or greenish depending on the relative intensities of the green and red channels.