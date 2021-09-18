import cv2
import numpy as np

img = cv2.imread('../images/test_img.png')

print(img[10][10])

cv2.imshow('Hello World', img)
cv2.waitKey(0)
cv2.destroyAllWindows()