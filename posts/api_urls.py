from django.conf.urls import include, url
from posts.api import BlogViewSet, PostViewSet

from rest_framework.routers import DefaultRouter

#Api Router
router = DefaultRouter()

router.register('posts', PostViewSet)
router.register('blogs', BlogViewSet)


urlpatterns = [
    #Api de Posts
    url(r'1.0/', include(router.urls)),
]

