import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/test_img.png')

histogram = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.hist(img.ravel(), 256, [0, 256])
plt.show()

color = ['b', 'g', 'r']
for i in range(len(color)):
    histogram2 = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histogram2, color=color[i])
plt.show()