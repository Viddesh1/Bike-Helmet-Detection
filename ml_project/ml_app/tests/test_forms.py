import os

from django.conf import settings
from django.test import TestCase

from ml_app.forms import ImageForm


class ImageFormTestCase(TestCase):

    def test_image_form_valid(self):
        form_data = {
            "image": os.path.join(
                settings.BASE_DIR,
                "ml_app",
                "tests",
                "test_assets",
                "test_images",
                "bike_rider.jpg",
            ),
            "video": os.path.join(
                settings.BASE_DIR,
                "ml_app",
                "tests",
                "test_assets",
                "test_videos",
                "he2.mp4",
            ),
        }
        form = ImageForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_image_form_invalid(self):
        """Invalid form data (missing required feilds)"""
        form_data = {}
        form = ImageForm(data=form_data)
        self.assertTrue(form.is_valid())
