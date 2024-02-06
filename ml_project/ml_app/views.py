from django.shortcuts import render
from . forms import ImageForm
from . models import Image, PredImage
from . utils import predict_yolo_image
import os
from django.core.files import File
import time

# Create your views here.

def  index(request):
    # Getting all the uploaded images
    all_images = Image.objects.all()
    all_predictions = PredImage.objects.all()

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save(commit=False)

            # # Perform additional processing or predictions here
            # if image_instance.image:
                # image_path = os.path.join("media", "images", "bike_rider.jpg")
            #     # image_path = os.path.join("C:/webapp/ml_project/runs/detect/predict", "bike_rider.jpg")
                # processed_image_path = predict_yolo(image_path)
            #     image_instance.pred_image = processed_image_path

            #     # Save the instance to the database
            #     image_instance.save()

            image_instance = form.save()
            image_path = os.path.join("media", "images", "bike_rider.jpg")
            predict_yolo_image(image_path)
            video_path = os.path.join("media", "videos", "he2.mp4")
            predict_yolo_image(video_path)

            # image_instance  = Image(
            #     image = os.path.join("runs", "detect", "predict", "bike_rider.jpg"), 
            #     video = os.path.join("runs", "detect", "predict", "bike_rider.jpg"), 
            #     pred_image = os.path.join("runs", "detect", "predict", "bike_rider.jpg"), 
            #     pred_video =os.path.join("runs", "detect", "predict", "bike_rider.jpg")
            #     ) 
            # image_instance .save()
            # Create a PredImage instance with the Image instance as its primary key

            # pred_image_instance = PredImage(
            #     pred_image_id=image_instance, 
            #     pred_image=os.path.join("runs", "detect", "predict", "bike_rider.jpg"), 
            #     pred_video=os.path.join("runs", "detect", "predict", "bike_rider.jpg")
            #     )
            # pred_image_instance.save()
            
            pred_image_instance = PredImage(pred_image_id=image_instance)

            # Open the image file and assign it to the pred_image field
            pred_image_path = os.path.join("runs", "detect", "predict", "bike_rider.jpg")
            with open(pred_image_path, 'rb') as pred_image_file:
                pred_image_instance.pred_image.save(os.path.basename(pred_image_path), File(pred_image_file))

            
            # time.sleep(2)
            pred_video_path = os.path.join("runs", "detect", "predict2", "he2.avi")
            with open(pred_video_path, 'rb') as pred_video_file:
                pred_image_instance.pred_video.save(os.path.basename(pred_video_path), File(pred_video_file))

            # Save the PredImage instance
            pred_image_instance.save()
            
    else:
        form = ImageForm()
    
    return render(request, 'ml_app/index.html', {'form': form, 'all_images': all_images, 'all_predictions': all_predictions}) 

