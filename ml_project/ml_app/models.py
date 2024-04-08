from django.db import models


# Create your models here.
class Image(models.Model):
    """
    Image model representation.
    
    Attributes:
    - id: AutoField, primary key for the image entry.
    - image: ImageField, the image file.
    - video: FileField, the video file associated with the image.

    Returns:
        str: A string representation of the image entry.
    """
    id = models.AutoField(primary_key=True)
    image = models.ImageField(
        upload_to="images", blank=False, null=False, default="Default Image"
    )
    video = models.FileField(
        upload_to="videos", blank=False, null=False, default="Default Video"
    )

    def __str__(self) -> str:
        """
        Return a string representation of the image entry.

        Returns:
        - str: A string representation in the format 'id - Image: image_path - Video: video_path'.
        """
        return f"{self.id} - Image: {self.image} - Video: {self.video}"


class PredImage(models.Model):
    """
    PredImage model inheriting from the model.Model.

    Attributes:
    - pred_image_id: OneToOneField to the Image model, primary key for the prediction entry.
    - pred_image: ImageField, the predicted image file.
    - pred_video: FileField, the predicted video file associated with the prediction.

    Returns:
        str: A string representation of the prediction entry.
    """
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
        """
        Return a string representation of the prediction entry.

        Returns:
        - str: A string representation in the format 'Prediction for Image id - Pred_image: pred_image_path - Pred_video: pred_video_path'.
        """
        return f"Prediction for Image {self.pred_image_id.id} - Pred_image: {self.pred_image} - Pred_video: {self.pred_video}"
