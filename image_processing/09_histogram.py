import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/test_img.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('img', gray)
histogram = cv2.calcHist([gray], [0], None, [256], [0, 256])

plt.title("Histogram of gray image")
plt.plot(histogram)
plt.figure()

color = ['b', 'g', 'r']
plt.title("Histogram of BGR image")
for i in range(len(color)):
    histogram2 = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histogram2, color=color[i])
plt.show()
cv2.waitKey(-1)
