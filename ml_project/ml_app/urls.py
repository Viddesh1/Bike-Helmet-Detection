from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers

from . import views
from .views import ImageViewSet, PredImageViewSet

router = routers.DefaultRouter()
router.register(r"images", ImageViewSet, basename="images")
router.register(r"predimages", PredImageViewSet, basename="predimages")


urlpatterns = [
    path("", views.index, name="index"),
    path("api/", include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
