import cv2
import numpy as np

img = cv2.imread('../images/test_img.png')

resized = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_AREA)

cv2.imshow('original', img)
cv2.imshow('resized', resized)

cv2.waitKey(0)
cv2.destroyAllWindows()