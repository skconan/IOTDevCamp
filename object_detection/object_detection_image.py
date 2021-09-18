import os
import cv2
import numpy as np

# Initialize Objects and corresponding colors which the model can detect
labels = ["background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow",
          "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
colors = np.random.uniform(0, 255, size=(len(labels), 3))

# Define paths
prototxt_path = '../object_detection/model_data/SSD_MobileNet_prototxt.txt'
caffemodel_path = '../object_detection/model_data/SSD_MobileNet.caffemodel'

# Read the model
model = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)

# Read image
frame = cv2.imread('../object_detection/test1.jpg')

# Get height and width of image
(h, w) = frame.shape[:2]
# Converting Frame to Blob
blob = cv2.dnn.blobFromImage(cv2.resize(
    frame, (300, 300)), 0.007843, (300, 300), 127.5)
# Passing Blob through network to detect and predict
model.setInput(blob)
detections = model.forward()
# Loop over the detections
for i in np.arange(0, detections.shape[2]):
    # Extracting the confidence of predictions
    confidence = detections[0, 0, i, 2]
    # Filtering out weak predictions
    if confidence > 0.6:

        # Extracting the index of the labels from the detection
        # Computing the (x,y) - coordinates of the bounding box
        idx = int(detections[0, 0, i, 1])
    # Extracting bounding box coordinates
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
    # Drawing the prediction and bounding box
        label = "{}: {:.2f}%".format(labels[idx], confidence * 100)
        cv2.rectangle(frame, (startX, startY), (endX, endY), colors[idx], 2)

        y = startY - 15 if startY - 15 > 15 else startY + 15
        cv2.putText(frame, label, (startX, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, colors[idx], 2)

cv2.imshow("Frame", frame)
key = cv2.waitKey(-1) & 0xFF
cv2.destroyAllWindows()
cv2.imwrite("out.jpg", frame)
