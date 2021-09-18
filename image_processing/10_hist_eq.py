import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./images/test_img.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

eq = cv2.equalizeHist(gray)

cv2.imshow('grayscale', gray)
cv2.imshow('histogram equalization', eq)

cv2.waitKey(0)
cv2.destroyAllWindows()