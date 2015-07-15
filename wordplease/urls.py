"""wordplease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from posts.views import HomeView, DetailView, BlogsListView, BlogDetailView, CreatePostView
from users.views import LoginView, LogOutView, SignupView
#from users.api import UserListAPI
from posts.api import BlogListAPI, PostsListApi, PostsDetailApi
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),


    # Este es el redireccionamiento de la parte de Blog & posts


    url(r'^home$', HomeView.as_view(), name='posts_home'),
    url(r'^$', HomeView.as_view(), name='posts_home'),
    url(r'^blogs/(?P<blog_id>[0-9]+)/(?P<post_identifier>[0-9]+)$', DetailView.as_view(), name='posts_detail'),

    #Blogs
    url(r'^blogs$', BlogsListView.as_view(), name='blogs_list'),
    url(r'^blogs/(?P<pk>[0-9]+)$', BlogDetailView.as_view(), name='blog_detail'),

    #Crear un Post
    url(r'^new-post$', login_required(CreatePostView.as_view()), name='posts_create_post'),


    #Este es el redireccionamiento de la parte de users
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogOutView.as_view(), name='users_logout'),
    url(r'^signup$', SignupView.as_view(), name='users_signup'),


    #Api de usuarios
    #url(r'^api/1.0/users/$', UserListAPI.as_view(), name='users_list_api'),

    #Api de Blogs
    url(r'^api/1.0/blogs/$', BlogListAPI.as_view(), name='blogs_api'),


    #Api de Posts
    url(r'^api/1.0/posts/$', PostsListApi.as_view(), name='posts_list_api'),
    url(r'^api/1.0/posts/(?P<pk>[0-9]+)$', PostsDetailApi.as_view(), name='posts_detail_api'),
]

