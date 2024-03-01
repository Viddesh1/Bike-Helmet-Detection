from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from .views import ImageViewSet, PredImageViewSet

router = routers.DefaultRouter()
router.register(r'images', ImageViewSet)
router.register(r'predimages', PredImageViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

