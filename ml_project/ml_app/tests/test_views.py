import os

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase
from django.urls import reverse


class ImageViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_view_get(self):
        """Test GET request to index view"""
        response = self.client.get(reverse(viewname="index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response=response, template_name="ml_app/index.html")

    # def test_index_view_post(self): # # This test is working fine!
    #     """Test POST request to index view"""
    #     # preparing form data
    #     image_path = os.path.join(settings.BASE_DIR, "ml_app", "tests", "test_assets", "test_images", "bike_rider.jpg")
    #     video_path = os.path.join(settings.BASE_DIR, "ml_app", "tests", "test_assets", "test_videos", "he2.mp4")

    #     with open(image_path, 'rb') as image_file, open(video_path, 'rb') as video_file:
    #         image = SimpleUploadedFile('bike_rider.jpg', image_file.read(), content_type='image/jpeg')
    #         video = SimpleUploadedFile('he2.mp4', video_file.read(), content_type='video/mp4')
    #         form_data = {
    #             'image': image,
    #             'video': video,
    #         }

    #         response = self.client.post(reverse('index'), form_data)

    #     self.assertEqual(response.status_code, 200)
