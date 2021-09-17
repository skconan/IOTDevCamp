# Import libraries
import os
import cv2
import time
import numpy as np

# Define paths
prototxt_path = os.path.join('/home/pi/IOTDevCamp/face_detection/model_data/deploy.prototxt')
caffemodel_path = os.path.join('/home/pi/IOTDevCamp/face_detection/model_data/weights.caffemodel')

# Read the model
model = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)

# Loop through all images and strip out faces
cap = cv2.VideoCapture(0)

# Set image size from camera
cap.set(3, 640)
cap.set(4, 480)

while True:
	# Read image from camera
	ret, frame = cap.read()

	# ret is boolean True/False
	# True - able to read image from camera 
	# False - cannot read image from camera 
	if not ret:
		break

	# Create blur image
	# frame_blur_bg = frame.copy()
	# frame_blur_bg = cv2.blur(frame_blur_bg, (21,21))

	# Get height and width of image
	(h, w) = frame.shape[:2]


	blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

	model.setInput(blob)
	detections = model.forward()

	# Identify each face
	for i in range(0, detections.shape[2]):
		# compute the (x, y)-coordinates of the bounding box for the object
		box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
		(startX, startY, endX, endY) = box.astype("int")

		width_face, height_face = endX - startX, endY

		confidence = detections[0, 0, i, 2]

		if (confidence > 0.8):				
			# frame_blur_bg[startY:endY, startX:endX] = frame[startY:endY, startX:endX].copy()
			
			cv2.putText(frame, '%.2f'%(confidence*100), (startX, startY), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)
			cv2.rectangle(frame, (startX, startY), (endX, endY), (0,255,0),2)
			# cv2.putText(frame_blur_bg, '%.2f'%(confidence*100), (startX, startY), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)
			# cv2.rectangle(frame_blur_bg, (startX, startY), (endX, endY), (0,255,0),2)

	cv2.imshow('image', cv2.resize(frame,None,fx=.5, fy=.5))
	# cv2.imshow('image', cv2.resize(frame_blur_bg,None,fx=.5, fy=.5))
	
	k = 0xff & cv2.waitKey(10)
	if k == ord('q'):
		break

cv2.destroyAllWindows()
