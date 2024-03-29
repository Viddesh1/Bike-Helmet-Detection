from rest_framework import serializers

from .models import Image, PredImage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "image", "video"]
        extra_kwargs = {"image": {"required": True}, "video": {"required": True}}


class PredImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredImage
        fields = ["pred_image_id", "pred_image", "pred_video"]
