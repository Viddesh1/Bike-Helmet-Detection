from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ml_app.views import index
from django.conf import settings
import os

class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)
