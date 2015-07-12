#-*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=150, default="")


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name

class Post(models.Model):
    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=150)
    summary = models.TextField(default="")
    body = models.TextField(default="")
    url_image = models.URLField(null=True)
    published_date = models.DateField()
    categories = models.ManyToManyField(Category)

    def __unicode__(self):
        return self.title


