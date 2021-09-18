import cv2
import numpy as np

img = cv2.imread('./images/test_img.png')

font = cv2.FONT_HERSHEY_SIMPLEX
fontsize = 2

img = cv2.putText(img, 'OpenCV', (50, 50), font, fontsize, (0, 0, 255), 2)

cv2.imshow('add text', img)

cv2.waitKey(0)
cv2.destroyAllWindows()