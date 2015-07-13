#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from posts.models import Post, Blog


class HomeView(View):

    def get(self, request):
        posts = Post.objects.all().order_by('-published_date')
        context = {
            'posts_list': posts
        }
        return render(request, 'posts/home.html', context)


class DetailView(View):

    def get(self, request, blog_id, post_identifier):
        possible_post = Post.objects.filter(pk=post_identifier).select_related('blog')
        post = possible_post[0] if len(possible_post)>0 else None

        if post is not None:
            context = {
                'post': post
            }
            return render(request, 'posts/detail.html', context)
        else:
            context = {
                'post_id': post_identifier
            }
            return render(request, 'posts/empty_detail.html', context)


class BlogsListView(View):
    def get(self, request):
        context = {
            'blogs_list': Blog.objects.all().order_by('name')
        }
        return render(request, 'posts/blogs_list.html', context)


class BlogDetailView(View):

    def get(self, request, pk):

        possible_post = Post.objects.filter(blog_id=pk).order_by('-published_date')

        context = {
            'posts_list': possible_post,
        }
        return render(request, 'posts/blogs_detail.html', context)