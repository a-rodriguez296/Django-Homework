#-*- coding: utf-8 -*-
from django.contrib.auth.models import User
from posts.models import Blog
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'id', 'password')