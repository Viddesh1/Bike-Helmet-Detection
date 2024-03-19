from ultralytics import YOLO
import os

def predict_yolo_image(path):
    model_path = YOLO(os.path.join('ml_app', 'weights', 'best.pt'))
    model_path.predict(path, save=True, imgsz=320, conf=0.5)

# stream = True is not working for some reason.
# def predict_yolo_video(path):
#     model_path = YOLO(os.path.join('ml_app', 'weights', 'best.pt'))
#     model_path.predict(path, save=True, imgsz=320, conf=0.5, stream = True)
    

def upload_image_video(dir_name):
    if str(dir_name) == "images":
        user_file_path = os.path.join("media", "images")
        newest_user_image = max([f for f in os.listdir(user_file_path) if os.path.isfile(os.path.join(user_file_path, f))], key=lambda x: os.path.getctime(os.path.join(user_file_path, x)))
        return newest_user_image
    
    if str(dir_name) == "videos":
        user_video_path = os.path.join("media", "videos")
        newest_user_video = max([f for f in os.listdir(user_video_path) if os.path.isfile(os.path.join(user_video_path, f))], key=lambda x: os.path.getctime(os.path.join(user_video_path, x)))
        return newest_user_video
    

def image_video_path():
    src_path = os.path.join("runs", "detect")
    # Find the newest directory in src
    newest_directory = max([d for d in os.listdir(src_path) if os.path.isdir(os.path.join(src_path, d))], key=lambda x: os.path.getctime(os.path.join(src_path, x)))
    # Path to the newest directory
    newest_directory_path = os.path.join(src_path, newest_directory)
    # Find the newest file inside the newest directory
    newest_file = max([f for f in os.listdir(newest_directory_path) if os.path.isfile(os.path.join(newest_directory_path, f))], key=lambda x: os.path.getctime(os.path.join(newest_directory_path, x)))
    return newest_directory, newest_file