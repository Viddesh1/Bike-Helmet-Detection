from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from .views import ImageViewSet, PredImageViewSet


from knox.views import LoginView as KnoxLoginView
from rest_framework import permissions


router = routers.DefaultRouter()
router.register(r'images', ImageViewSet)
router.register(r'predimages', PredImageViewSet)

class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)  # Allow any user to login

urlpatterns = [
    path("", views.index, name="index"),
    path('api/', include(router.urls)),
    path('api/auth/login/', LoginView.as_view(), name='knox_login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

