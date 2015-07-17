#-*- coding: utf-8 -*-

from rest_framework import serializers
from models import Post, Blog, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name',)


class PostSerializer(serializers.ModelSerializer):
    #categories = CategorySerializer(many=True,)

    # def create(self, validated_data):
    #     categories = validated_data.pop('categories')
    #     for category_dict in categories:
    #         category_object =Category.objects.filter(name=category_dict.get('name'))[0]
    #
    #     post = Post.objects.create(**validated_data)
    #
    #
    #
    #     request = self.context.get('request')
    #     post.blog = request.user.blog
    #
    #     return post

    class Meta:
        model = Post
        #fields = ('title','summary', 'url_image', 'published_date', 'body', 'blog')


class BlogSerializer(serializers.ModelSerializer):

    posts_set = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='posts-detail',
    )

    class Meta:
        model = Blog
        fields =("name", "posts_set")