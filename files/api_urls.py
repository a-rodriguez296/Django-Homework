from django.conf.urls import include, url
from api import FileViewSet

from rest_framework.routers import DefaultRouter

#Api Router
router = DefaultRouter()

router.register('files', FileViewSet)


urlpatterns = [
    #Api de Posts
    url(r'1.0/', include(router.urls)),
]