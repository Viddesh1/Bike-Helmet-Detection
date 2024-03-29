from django.db import models


# Create your models here.
class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(
        upload_to="images", blank=False, null=False, default="Default Image"
    )
    video = models.FileField(
        upload_to="videos", blank=False, null=False, default="Default Video"
    )

    def __str__(self):
        return f"{self.id} - Image: {self.image} - Video: {self.video}"


class PredImage(models.Model):
    pred_image_id = models.OneToOneField(
        Image, primary_key=True, on_delete=models.CASCADE
    )
    pred_image = models.ImageField(
        upload_to="pred_images", blank=False, null=False, default="Default pred Image"
    )
    pred_video = models.FileField(
        upload_to="pred_videos", blank=False, null=False, default="Default pred Video"
    )

    def __str__(self):
        return f"Prediction for Image {self.pred_image_id.id} - Pred_image: {self.pred_image} - Pred_video: {self.pred_video}"
