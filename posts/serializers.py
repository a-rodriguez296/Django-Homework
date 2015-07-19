#-*- coding: utf-8 -*-

from rest_framework import serializers
from django.core.urlresolvers import reverse
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

class PostSerializerUrl(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, instance):

        return reverse('posts_detail', args=[instance.blog.id, instance.id])

    class Meta:
        model = Post
        fields = ('url', )

class BlogSerializer(serializers.ModelSerializer):

    post_set=PostSerializerUrl(many=True)

    class Meta:
        model = Blog
        fields =("name", "post_set")
