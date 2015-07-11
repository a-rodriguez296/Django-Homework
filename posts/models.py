#-*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=150)
    summary = models.TextField(default="")
    body = models.TextField(default="")
    url_image = models.URLField(null=True)
    published_date = models.DateField()

    def __unicode__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=150)
    post = models.ForeignKey(Post)