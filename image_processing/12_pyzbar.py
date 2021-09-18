import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

img = cv2.imread('../images/barcode.png')


decodedObjects = pyzbar.decode(img)
for obj in decodedObjects:
    print(obj.data.decode('utf-8'))
    print(obj.type)
    print(obj.rect)
    print(obj.polygon)

cv2.imshow('barcode', img)
cv2.waitKey(0)