from django.shortcuts import render
from . forms import ImageForm
from . models import Image, PredImage
from . utils import predict_yolo_image, upload_image_video, image_video_path
import os
from django.core.files import File
import shutil


def  index(request):
    all_images = Image.objects.all()
    all_predictions = PredImage.objects.all()

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            # image_instance = form.save(commit=False)
            image_instance = form.save()

            # Getting the newest image file present in media/images directory.
            newest_user_image = upload_image_video(dir_name = "images")
            image_path = os.path.join("media", "images", newest_user_image)
            predict_yolo_image(image_path) 
            newest_directory, newest_file = image_video_path()
            
            #  Getting the newest video file present in media/images directory.
            newest_user_video = upload_image_video(dir_name = "videos")
            video_path = os.path.join("media", "videos", newest_user_video)
            predict_yolo_image(video_path)
            newest_video_directory, newest_video_file = image_video_path()
            pred_image_instance = PredImage(pred_image_id=image_instance)

            # Open the image file and assign it to the pred_image field
            pred_image_path = os.path.join("runs", "detect", newest_directory, newest_file)
            with open(pred_image_path, 'rb') as pred_image_file:
                pred_image_instance.pred_image.save(os.path.basename(pred_image_path), File(pred_image_file))
            
            # Open the video file and assign it to the pred_video field
            pred_video_path = os.path.join("runs", "detect", newest_video_directory, newest_video_file)
            with open(pred_video_path, 'rb') as pred_video_file:
                pred_image_instance.pred_video.save(os.path.basename(pred_video_path), File(pred_video_file))

            # Save the PredImage instance
            pred_image_instance.save()

            # Deleting all the predicted images and videos by YOLO model to save memory.
            shutil.rmtree(path = os.path.join("runs", "detect"))
            
    else:
        form = ImageForm()
    
    return render(request, 'ml_app/index.html', {'form': form, 'all_images': all_images, 'all_predictions': all_predictions}) 



