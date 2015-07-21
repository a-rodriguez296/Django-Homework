#-*- coding: utf-8 -*-


from rest_framework import filters, mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from models import Post, Blog
from serializers import BlogSerializer, PostSerializerList, PostSerializerCreate, PostSerializerDetail
from rest_framework.viewsets import ModelViewSet


class BlogViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name', )
    ordering = ('name',)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('title', 'published_date')
    ordering = ('-published_date', )

    def get_queryset(self):

        #Si el usuario no esta autenticado, se muestran los posts que tienen status publicado
        if not self.request.user.is_authenticated():
            query_set = Post.objects.filter(is_published=True)
        else:

            #Si el usuario es superuser, se muestan todos los posts
            if self.request.user.is_superuser:
                query_set = Post.objects.all()
            #Si el usuario no es superuser, pero está autenticado, se le muestran sólo los posts de él.
            else:
                query_set = Post.objects.filter(blog__owner=self.request.user)
        return query_set

    def get_serializer_class(self):
        if self.action == 'list':
            return PostSerializerList
        elif self.action == 'create':
            return PostSerializerCreate
        else:
            return PostSerializerDetail

    def perform_create(self, serializer):

        #Acá tengo que asignar el blog
        serializer.save(blog=self.request.user.blog)


# class BlogListAPI(ListAPIView):
#     serializer_class = BlogSerializer
#     queryset = Blog.objects.all()
#     filter_backends = (filters.SearchFilter, filters.OrderingFilter)
#     search_fields = ('name', )
#     ordering = ('name', )

# class PostsListApi(ListCreateAPIView):
#
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#     filter_backends = (filters.SearchFilter, filters.OrderingFilter)
#     search_fields = ('title', 'published_date')
#     ordering = ('-published_date', )
#
#     def perform_create(self, serializer):
#
#         #Acá tengo que asignar el blog
#         serializer.save(blog=self.request.user.blog)
#
#     def get_serializer_class(self):
#         return PostSerializerList if self.request.method == 'GET' else PostSerializerCreate
#
#     def get_queryset(self):
#
#         #Si el usuario no esta autenticado, se muestran los posts que tienen status publicado
#         if not self.request.user.is_authenticated():
#             query_set = Post.objects.filter(is_published=True)
#         else:
#
#             #Si el usuario es superuser, se muestan todos los posts
#             if self.request.user.is_superuser:
#                 query_set = Post.objects.all()
#             #Si el usuario no es superuser, pero está autenticado, se le muestran sólo los posts de él.
#             else:
#                 query_set = Post.objects.filter(blog__owner=self.request.user)
#         return query_set
#
#
# class PostsDetailApi(RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#     serializer_class = PostSerializerDetail
#
#     def get_queryset(self):
#         if not self.request.user.is_authenticated():
#             query_set = Post.objects.filter(is_published=True)
#         else:
#             if self.request.user.is_superuser:
#                 query_set = Post.objects.all()
#             else:
#                 query_set = Post.objects.filter(blog__owner=self.request.user)
#         return query_set