from django.conf import settings
from django.contrib.staticfiles.views import serve
from django.test import SimpleTestCase
from django.urls import resolve, reverse

from ml_app.views import index


class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse("index")
        self.assertEqual(resolve(url).func, index)

    def test_settings_debug_true(self):
        from ml_app.urls import settings as urls_settings

        self.assertEqual(first=settings.DEBUG, second=urls_settings.DEBUG)
