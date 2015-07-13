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
from posts.views import HomeView, DetailView, BlogsListView, BlogDetailView
from users.views import LoginView, LogOutView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),


    # Este es el redireccionamiento de la parte de Blog & posts


    url(r'^home$', HomeView.as_view(), name='posts_home'),
    url(r'^blogs/(?P<blog_id>[0-9]+)/(?P<post_identifier>[0-9]+)$', DetailView.as_view(), name='posts_detail'),

    #Blogs
    url(r'^blogs$', BlogsListView.as_view(), name='blogs_list'),
    url(r'^blogs/(?P<pk>[0-9]+)$', BlogDetailView.as_view(), name='blog_detail'),


    #Este es el redireccionamiento de la parte de users
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogOutView.as_view(), name='users_logout'),

]

