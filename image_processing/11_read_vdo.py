import cv2
import numpy as np

cap = cv2.VideoCapture('../images/cargo_drone.mp4')

while(True):
    
    ret, frame = cap.read()
    if ret == True:
        
        cv2.imshow('frame', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()