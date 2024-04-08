from rest_framework import serializers

from .models import Image, PredImage


class ImageSerializer(serializers.ModelSerializer):
    """
    Serializer for the Image model inherited from serializer.ModelSerializer.

    Meta:
    - model: Image, the model associated with the serializer Image class.
    - fields: List of fields from the model to include in the serializer.
    - extra_kwargs: Additional keyword arguments for customizing field behavior.

    Attributes od class Meta:
    - model: Image instance of the class Image
    - fields:
        - id: IntegerField, the ID of the image.
        - image: ImageField, the image file.
        - video: FileField, the video file associated with the image.
    - extra_kwargs:
        - image: image field is required in application programming interface (API).
        - video: video field is required in application programming interface (API).
    """
    class Meta:
        model = Image
        fields = ["id", "image", "video"]
        extra_kwargs = {"image": {"required": True}, "video": {"required": True}}


class PredImageSerializer(serializers.ModelSerializer):
    """
    Serializer for the PredImage model inherited from serializer.ModelSerializer

    Meta:
    - model: Image, the model associated with the serializer PredImage class.
    - fields: List of fields from the model to include in the serializer.
    """
    class Meta:
        model = PredImage
        fields = ["pred_image_id", "pred_image", "pred_video"]
