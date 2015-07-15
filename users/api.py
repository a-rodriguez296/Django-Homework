#-*- coding: utf-8 -*-

from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from django.contrib.auth.models import User
from serializer import UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class UserCreateApi(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)





class UserDetialApi(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        if self.request.user.is_authenticated():
            if self.request.user.is_superuser:
                return User.objects.all()
            else:
                return User.objects.filter(pk=self.request.user.id)
        else:
            return None





