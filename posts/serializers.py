#-*- coding: utf-8 -*-

from rest_framework import serializers
from django.core.urlresolvers import reverse
from models import Post, Blog, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name',)


class PostSerializerBase(serializers.ModelSerializer):

    class Meta:
        model = Post


class PostSerializerList(PostSerializerBase):

    class Meta(PostSerializerBase.Meta):
        fields = ('title', 'url_image', 'summary', 'published_date')


class PostSerializerCreate(PostSerializerBase):

    class Meta(PostSerializerBase.Meta):
        exclude = ('blog', )


class PostSerializerUrl(PostSerializerBase):
    url = serializers.SerializerMethodField()

    def get_url(self, instance):

        return reverse('posts_detail', args=[instance.blog.id, instance.id])

    class Meta(PostSerializerBase.Meta):
        #model = Post
        fields = ('url', )


class BlogSerializer(serializers.ModelSerializer):

    post_set=PostSerializerUrl(many=True)

    class Meta:
        model = Blog
        fields =("name", "post_set")
