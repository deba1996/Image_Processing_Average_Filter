import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Image 6.JPG')#read the input image

blur = cv2.blur(img,(5,5))#apply the average blurring method

plt.subplot(121),plt.imshow(img),plt.title('Original')#show the original image
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')#show the blurred image
plt.xticks([]), plt.yticks([])
plt.show()
