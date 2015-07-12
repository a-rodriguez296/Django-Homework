#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from posts.models import Post


class HomeView(View):

    def get(self, request):
        posts = Post.objects.all().order_by('published_date')
        context = {
            'posts_list': posts
        }
        return render(request, 'posts/home.html', context)

class DetailView(View):

    def get(self, request, pk):
        possible_post = Post.objects.filter(pk=pk).select_related('owner')
        post = possible_post[0] if len(possible_post)>0 else None

        if post is not None:
            context = {
                'post': post
            }
            return render(request, 'posts/detail.html', context)