import cv2
import numpy as np

img = cv2.imread('../images/test_img.png')

img = cv2.rectangle(img, (50, 50), (200, 300), (255, 0, 0), 2)
img = cv2.circle(img, (250, 250), 60, (0, 255, 0), -1)
img = cv2.line(img, (100, 100), (500, 500), (0, 0, 255), 5)

cv2.imshow('draw', img)

cv2.waitKey(0)
cv2.destroyAllWindows()