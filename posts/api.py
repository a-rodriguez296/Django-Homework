#-*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from models import Post, Blog
from serializers import BlogSerializer, PostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class BlogListAPI(ListAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )


class PostsListApi(ListCreateAPIView):

    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'body')
    ordering = ('title', 'published_date')

    def perform_create(self, serializer):

        #Acá tengo que asignar el blog
        serializer.save(blog=self.request.user.blog)

    def get_queryset(self):

        query_set = None
        if not self.request.user.is_authenticated():
            query_set = Post.objects.filter(is_published=True)
        else:
            if self.request.user.is_superuser:
                query_set = Post.objects.all()
            else:
               query_set = Post.objects.filter(blog__owner=self.request.user)
        return query_set




        #query_set = None

        #Definir si es List o Create
        # if self.request.method == 'GET':
        #     if not self.request.user.is_authenticated():
        #         query_set = Post.objects.filter(is_published=True)
        #     else:
        #         #Caso en el que es admin y no llega nada en la busqueda
        #         if self.request.user.is_superuser and not self.request.GET.get('search'):
        #             query_set = Post.objects.all()
        #
        #
        #         #Caso en el que es admin y llega algo en el la busqueda
        #         elif self.request.user.is_superuser:
        #             #todo Como hago para no repetir el query
        #             query_set = Post.objects.filter(Q(title__icontains=self.request.GET.get('search')) | Q(body__icontains=self.request.GET.get('search')))
        #
        #
        #         #Caso de usuario cualquiera
        #         else:
        #             query_set = Post.objects.filter(blog__owner=self.request.user)
        #     if self.request.GET.get('search'):
        #         query_set.filter(Q(title__icontains=self.request.GET.get('search')) | Q(body__icontains=self.request.GET.get('search')))
        # else:
        #     query_set = Post.objects.all()
        # return query_set



class PostsDetailApi(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer