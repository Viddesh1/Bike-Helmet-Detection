from django.db import models
import os

# Create your models here.
class Image(models.Model):
    id = models.AutoField(primary_key = True)
    image = models.ImageField(upload_to="images", blank = True, null = True)
    video = models.FileField(upload_to = "videos", blank = True, null = True)
    

    def __str__(self):
        return f"{self.id} - Image: {self.image} - Video: {self.video}"
    

class PredImage(models.Model):
    pred_image_id = models.OneToOneField(Image, primary_key = True, on_delete = models.CASCADE)
    pred_image = models.ImageField(upload_to="pred_images", blank=True, null=True)
    pred_video = models.FileField(upload_to="pred_videos", blank=True, null=True)

    def __str__(self):
        return f"Prediction for Image {self.pred_image_id.id} - Pred_image: {self.pred_image} - Pred_video: {self.pred_video}"
    
    
