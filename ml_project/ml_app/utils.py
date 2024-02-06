from ultralytics import YOLO
import os

def predict_yolo_image(path):
    model_path = YOLO(os.path.join('ml_app', 'weights', 'best.pt'))
    model_path.predict(path, save=True, imgsz=320, conf=0.5)

# stream = True is not working for some reason.
# def predict_yolo_video(path):
#     model_path = YOLO(os.path.join('ml_app', 'weights', 'best.pt'))
#     model_path.predict(path, save=True, imgsz=320, conf=0.5, stream = True)