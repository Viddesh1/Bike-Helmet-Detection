from ultralytics import YOLO
# from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2

model = YOLO("weights/best.pt")

# Make sure Webcam is connected and working correctly.
# This code will open webcam to run YOLOv8 inference upon
# Highly dependent upon computational speed and camera quality fps too!.
result = model.predict(source = "0", stream=True, show=True) # save=True, imgsz=320, conf=0.5
# print(result)
for r in result:
    boxes = r.boxes  # Boxes object for bbox outputs
    masks = r.masks  # Masks object for segment masks outputs
    probs = r.probs  # Class probabilities for classification outputs
    # print(r)
