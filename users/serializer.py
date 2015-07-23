#-*- coding: utf-8 -*-
from django.contrib.auth.models import User
from posts.models import Blog
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'id', 'password')

# class UserSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     username = serializers.CharField()
#     email = serializers.CharField()
#     password = serializers.CharField()
#
#     #Los serializadores deben definir dos métodos obligatoriamente, create y update
#
#     def create(self, validated_data):
#
#         instance = User()
#         return self.update(instance, validated_data)
#
#     def update(self, instance, validated_date):
#
#         instance.first_name = validated_date.get('first_name')
#         instance.last_name = validated_date.get('last_name')
#         instance.username = validated_date.get('username')
#         instance.email = validated_date.get('email')
#
#         #En caso de la contraseña hay que condificarla
#         instance.set_password(validated_date.get('password'))
#
#         instance.save()
#
#         return instance
#
#     #En este caso en data llega solo el username. Si fuera def validate llegaria toda la info en un diccionario
#     def validate_username(self, data):
#
#         users = User.objects.filter(username=data)
#
#         #Si estoy creando un usuario "not self.instance" && ya existe algun usuario con ese username len(users) != 0
#         if not self.instance and len(users) != 0:
#             raise serializers.ValidationError("Ya existe un usuario con ese username")
#         #Si estoy acutalizando un usuario y el nombre de usuario ya existe
#         elif self.instance and len(users) != 0:
#             raise serializers.ValidationError("Ya existe un usuario con ese username")
#         #Si estoy creando o actualizando y el nombre de usuario no existe
#         else:
#             return data