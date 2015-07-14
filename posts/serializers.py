#-*- coding: utf-8 -*-

from rest_framework import serializers
from models import Post, Blog


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog

    #Me hace falta cómo generar la url de los posts hijos del blog