#-*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from models import Post, Blog
from serializers import BlogSerializer, PostSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Q

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

    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):

        query_set = None

        #Definir si es List o Create
        if self.request.method == 'GET':
            if not self.request.user.is_authenticated():
                query_set = Post.objects.filter(is_published=True)
            else:
                #Caso en el que es admin y no llega nada en la busqueda
                if self.request.user.is_superuser and not self.request.GET.get('search'):
                    query_set = Post.objects.all()


                #Caso en el que es admin y llega algo en el la busqueda
                elif self.request.user.is_superuser:
                    #todo Como hago para no repetir el query
                    query_set = Post.objects.filter(Q(title__icontains=self.request.GET.get('search')) | Q(body__icontains=self.request.GET.get('search')))


                #Caso de usuario cualquiera
                else:
                    query_set = Post.objects.filter(blog__owner=self.request.user)
            if self.request.GET.get('search'):
                query_set.filter(Q(title__icontains=self.request.GET.get('search')) | Q(body__icontains=self.request.GET.get('search')))
        else:
            pass
        return query_set





class PostsDetailApi(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer