from rest_framework import serializers
from . models import Image, PredImage

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

    def create(self, validated_data):
        return Image.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.video = validated_data.get('video', instance.video)
        instance.save()
        return instance

class PredImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredImage
        fields = '__all__'

