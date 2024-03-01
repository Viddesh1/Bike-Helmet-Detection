from rest_framework import serializers
from . models import Image, PredImage

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class PredImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredImage
        fields = '__all__'

