import os

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from ml_app.models import Image, PredImage


# Bike-Helmet-Detection/ml_project/ml_app/tests/test_assets/test_images/bike_rider.jpg
class ImageModelTestCase(TestCase):

    def setUp(self):
        self.image = Image.objects.create(
            image=SimpleUploadedFile(
                name="test_image.jpg",
                content=open(
                    os.path.join(
                        settings.BASE_DIR,
                        "ml_app",
                        "tests",
                        "test_assets",
                        "test_images",
                        "bike_rider.jpg",
                    ),
                    "rb",
                ).read(),
                content_type="image/jpg",
            ),
            video=SimpleUploadedFile(
                name="test_video.mp4",
                content=open(
                    os.path.join(
                        settings.BASE_DIR,
                        "ml_app",
                        "tests",
                        "test_assets",
                        "test_videos",
                        "he2.mp4",
                    ),
                    "rb",
                ).read(),
                content_type="video/mp4",
            ),
        )

    def test_image_creation(self):
        """Testing that an image is created successfully."""
        self.assertEqual(self.image.id, 1)
        self.assertIsNotNone(self.image.image)
        self.assertIsNotNone(self.image.video)


class PredImageModelTestCase(TestCase):

    def setUp(self):
        self.image = Image.objects.create(
            image=SimpleUploadedFile(
                name="test_image.jpg",
                content=open(
                    os.path.join(
                        settings.BASE_DIR,
                        "ml_app",
                        "tests",
                        "test_assets",
                        "test_images",
                        "bike_rider.jpg",
                    ),
                    "rb",
                ).read(),
                content_type="image/jpg",
            ),
            video=SimpleUploadedFile(
                name="test_video.mp4",
                content=open(
                    os.path.join(
                        settings.BASE_DIR,
                        "ml_app",
                        "tests",
                        "test_assets",
                        "test_videos",
                        "he2.mp4",
                    ),
                    "rb",
                ).read(),
                content_type="video/mp4",
            ),
        )
        self.pred_image = PredImage.objects.create(
            pred_image_id=self.image,
            pred_image=SimpleUploadedFile(
                name="test_pred_image.jpg",
                content=open(
                    os.path.join(
                        settings.BASE_DIR,
                        "ml_app",
                        "tests",
                        "test_assets",
                        "test_images",
                        "bike_rider.jpg",
                    ),
                    "rb",
                ).read(),
                content_type="image/jpeg",
            ),
            pred_video=SimpleUploadedFile(
                name="test_pred_image.mp4",
                content=open(
                    os.path.join(
                        settings.BASE_DIR,
                        "ml_app",
                        "tests",
                        "test_assets",
                        "test_videos",
                        "he2.mp4",
                    ),
                    "rb",
                ).read(),
                content_type="video/mp4",
            ),
        )

    def test_pred_image_creation(self):
        """Testing that predicted image is created successfully"""
        self.assertEqual(self.pred_image.pred_image_id, self.image)
        self.assertIsNotNone(self.pred_image.pred_image)
        self.assertIsNotNone(self.pred_image.pred_video)
