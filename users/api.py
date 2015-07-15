#-*- coding: utf-8 -*-

from rest_framework.generics import CreateAPIView, ListCreateAPIView
from django.contrib.auth.models import User
from serializer import UserSerializer


class UserCreateApi(ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
