import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/qrcode2.jpg')

plt.figure()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.hist(gray.ravel(), 256, [0, 256])


plt.figure()
color = ['b', 'g', 'r']
for i in range(len(color)):
    histogram2 = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histogram2, color=color[i])

cv2.imshow('img', img)
cv2.imshow('gray', gray)
cv2.waitKey(0)
plt.show()
cv2.destroyAllWindows()

