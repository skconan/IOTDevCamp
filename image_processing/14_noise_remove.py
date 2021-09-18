import cv2
import numpy as np

img = cv2.imread('../images/img_noise.png')

cv2.imshow('img', img)
avg_blur = cv2.blur(img, (5, 5))
med_blur = cv2.medianBlur(img, 5)
gaun_blur = cv2.GaussianBlur(img, (5,5), sigmaX=2)

cv2.imshow('avg blur', avg_blur)
cv2.imshow('med blur', med_blur)
cv2.imshow('Gaussian blur', gaun_blur)
cv2.waitKey()
cv2.destroyAllWindows()