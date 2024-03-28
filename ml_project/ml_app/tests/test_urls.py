from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ml_app.views import index
from django.conf import settings
from django.test.client import RequestFactory
from django.contrib.staticfiles.views import serve


class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_settings_debug_true(self):
        from ml_app.urls import settings as urls_settings
        self.assertEqual(first=settings.DEBUG, second=urls_settings.DEBUG)

    def test_api_url_resolves(self):
        url = reverse('api-root/')
        self.assertEqual(resolve(url).view_name, 'api-root/')

    def test_media_url_serves(self):
        factory = RequestFactory()
        request = factory.get(settings.MEDIA_URL + 'test.txt')
        response = serve(request, 'test.txt', document_root=settings.MEDIA_ROOT)
        self.assertEqual(response.status_code, 200)

    def test_media_url_resolves(self):
        url = settings.MEDIA_URL + 'test.txt'
        self.assertEqual(resolve(url).url_name, 'django.contrib.staticfiles.views.serve')

    