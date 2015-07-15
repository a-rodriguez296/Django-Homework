#-*- coding: utf-8 -*-

from rest_framework import serializers
from models import Post, Blog


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post


class BlogSerializer(serializers.ModelSerializer):

    post_set = PostSerializer(many=True)

    class Meta:
        model = Blog