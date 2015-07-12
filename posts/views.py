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