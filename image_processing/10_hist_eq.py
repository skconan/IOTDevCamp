import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./images/test_img.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.figure()
plt.title("Histogram of Gray")
plt.hist(gray.ravel(), 256, [0, 256])


eq = cv2.equalizeHist(gray)

plt.figure()
plt.title("Histogram of Equalization")
plt.hist(eq.ravel(), 256, [0, 256])

cv2.imshow('grayscale', gray)
cv2.imshow('histogram equalization', eq)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()