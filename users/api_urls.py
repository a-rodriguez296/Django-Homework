from django.conf.urls import include, url
from users.api import UserCreateDetailUpdateDestroyViewSet
from rest_framework.routers import DefaultRouter

#Api Router
router = DefaultRouter()

router.register('users', UserCreateDetailUpdateDestroyViewSet)

urlpatterns = [
    #Api de Posts
    url(r'1.0/', include(router.urls)),

]

