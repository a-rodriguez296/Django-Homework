#-*- coding: utf-8 -*-

from rest_framework.serializers import ModelSerializer
from models import File

class FileSerializer(ModelSerializer):
    class Meta:
        model = File