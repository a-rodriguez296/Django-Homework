#-*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from models import Post, Blog
from serializers import BlogSerializer, PostSerializer
from rest_framework.response import Response


class BlogListAPI(APIView):

    def get(self, request):

        blog_name = request.GET.get('blog_name')

        if blog_name:
            blogs = Blog.objects.filter(name__icontains=blog_name).order_by('name')
        else:
            blogs = Blog.objects.all()

        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)


class PostsListApi(ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostsDetailApi(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer