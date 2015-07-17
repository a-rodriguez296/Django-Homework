#-*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.validators import ValidationError
from models import Post, Blog, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id',)


class PostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)


    # def create(self, validated_data):
    #     post = Post(**validated_data)
    #
    #     request = self.context.get('request')
    #     post.blog = request.user.blog
    #
    #     return post

    class Meta:
        model = Post
        fields = ('title','summary', 'url_image', 'published_date', 'categories', 'body', 'blog')


class BlogSerializer(serializers.ModelSerializer):

    post_set = PostSerializer(many=True)

    class Meta:
        model = Blog