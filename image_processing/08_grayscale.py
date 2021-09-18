import cv2
import numpy as np

img = cv2.imread('./images/test_img.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('original', img)
cv2.imshow('grayscale', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()