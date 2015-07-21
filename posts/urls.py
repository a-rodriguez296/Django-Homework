from django.conf.urls import  url
from posts.views import HomeView, DetailView, BlogsListView, BlogDetailView, CreatePostView

from django.contrib.auth.decorators import login_required

urlpatterns = [

    # Este es el redireccionamiento de la parte de Blog & posts


    url(r'^home$', HomeView.as_view(), name='posts_home'),
    url(r'^$', HomeView.as_view(), name='posts_home'),
    url(r'^blogs/(?P<blog_id>[0-9]+)/(?P<post_identifier>[0-9]+)$', DetailView.as_view(), name='posts_detail'),

    #Blogs
    url(r'^blogs$', BlogsListView.as_view(), name='blogs_list'),
    url(r'^blogs/(?P<pk>[0-9]+)$', BlogDetailView.as_view(), name='blog_detail'),

    #Crear un Post
    url(r'^new-post$', login_required(CreatePostView.as_view()), name='posts_create_post'),

]

