#-*- coding: utf-8 -*-

from rest_framework import serializers
from models import Post, Blog, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name',)


class PostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Post
        fields = ('title','summary', 'url_image', 'published_date', 'categories')


class BlogSerializer(serializers.ModelSerializer):

    post_set = PostSerializer(many=True)

    class Meta:
        model = Blog