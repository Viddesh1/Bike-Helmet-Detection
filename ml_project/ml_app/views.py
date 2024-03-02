from django.shortcuts import render
from . forms import ImageForm
from . models import Image, PredImage
from . utils import predict_yolo_image, upload_image_video, image_video_path
import os
from django.core.files import File
import shutil

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Image, PredImage
from .serializers import ImageSerializer, PredImageSerializer


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


# class ImageViewSet(viewsets.ModelViewSet):
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer

class PredImageViewSet(viewsets.ModelViewSet):
    queryset = PredImage.objects.all()
    serializer_class = PredImageSerializer    

# class PredImageViewSet(viewsets.ViewSet):
#     queryset = PredImage.objects.all()
#     serializer_class = PredImageSerializer    

#     def list(self, request):
#         pred_images = PredImage.objects.all()
#         serializer = self.serializer_class(pred_images, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             instance = serializer.save()

#             # Perform pre-processing for the image
#             newest_user_image = upload_image_video(dir_name="pred_images")
#             image_path = os.path.join("media", "pred_images", newest_user_image)
#             predict_yolo_image(image_path)
#             newest_directory, newest_file = image_video_path()

#             # Getting the newest video file present in media/pred_images directory.
#             newest_user_video = upload_image_video(dir_name="pred_videos")
#             video_path = os.path.join("media", "pred_videos", newest_user_video)
#             predict_yolo_image(video_path)
#             newest_video_directory, newest_video_file = image_video_path()

#             # Create PredImage instance
#             pred_image_instance = PredImage(pred_image_id=instance)

#             # Open the image file and assign it to the pred_image field
#             pred_image_path = os.path.join("runs", "detect", newest_directory, newest_file)
#             with open(pred_image_path, 'rb') as pred_image_file:
#                 pred_image_instance.pred_image.save(os.path.basename(pred_image_path), File(pred_image_file))

#             # Open the video file and assign it to the pred_video field
#             pred_video_path = os.path.join("runs", "detect", newest_video_directory, newest_video_file)
#             with open(pred_video_path, 'rb') as pred_video_file:
#                 pred_image_instance.pred_video.save(os.path.basename(pred_video_path), File(pred_video_file))

#             # Save the PredImage instance
#             pred_image_instance.save()

#             # Deleting all the predicted images and videos by YOLO model to save memory.
#             shutil.rmtree(path=os.path.join("runs", "detect"))

#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         pred_image = PredImage.objects.get(pk=pk)
#         serializer = self.serializer_class(pred_image)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         pred_image = PredImage.objects.get(pk=pk)
#         serializer = self.serializer_class(pred_image, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def partial_update(self, request, pk=None):
#         pred_image = PredImage.objects.get(pk=pk)
#         serializer = self.serializer_class(pred_image, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         pred_image = PredImage.objects.get(pk=pk)
#         pred_image.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# https://www.django-rest-framework.org/api-guide/viewsets/
# post request also deal with null fields automatically.
class ImageViewSet(viewsets.ViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def list(self, request):
        images = Image.objects.all()
        serializer = self.serializer_class(images, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()

            # Perform pre-processing for the image
            newest_user_image = upload_image_video(dir_name="images")
            image_path = os.path.join("media", "images", newest_user_image)
            predict_yolo_image(image_path)
            newest_directory, newest_file = image_video_path()

            #  Getting the newest video file present in media/images directory.
            newest_user_video = upload_image_video(dir_name = "videos")
            video_path = os.path.join("media", "videos", newest_user_video)
            predict_yolo_image(video_path)
            newest_video_directory, newest_video_file = image_video_path()

            # Create PredImage instance
            pred_image_instance = PredImage(pred_image_id=instance)

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

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        try:
            image = Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(image)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            image = Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            image = Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(image, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            image = Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
