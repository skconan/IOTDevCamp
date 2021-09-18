import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

img = cv2.imread("../images/qrcode2.jpg")

decodedObjects = pyzbar.decode(img)
for obj in decodedObjects:
    (x, y, w, h) = obj.rect
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
    data = obj.data.decode("utf-8")
    cv2.putText(img, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

cv2.imshow("Frame", img)
cv2.waitKey(0)
cv2.destroyAllWindows()