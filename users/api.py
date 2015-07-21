#-*- coding: utf-8 -*-

from django.contrib.auth.models import User
from serializer import UserSerializer
from rest_framework import mixins, viewsets
from posts.models import Blog


class UserCreateDetailUpdateDestroyViewSet(mixins.CreateModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.DestroyModelMixin,
                                mixins.UpdateModelMixin,
                                viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        blog = Blog()
        blog.name = "Blog de {}".format(user.username)
        blog.owner = user
        blog.save()

    def get_queryset(self):
        if self.request.user.is_authenticated():
            if self.request.user.is_superuser:
                return User.objects.all()
            else:
                return User.objects.filter(pk=self.request.user.id)
        else:
            return None



# class UserCreateApi(CreateAPIView):
#
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetailApi(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
#     def get_queryset(self):
#         if self.request.user.is_authenticated():
#             if self.request.user.is_superuser:
#                 return User.objects.all()
#             else:
#                 return User.objects.filter(pk=self.request.user.id)
#         else:
#             return None