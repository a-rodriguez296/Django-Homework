#-*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    usr = forms.CharField(label="Nombre de usuario")
    pwd = forms.CharField(label="Contraseña", widget=forms.PasswordInput())


class SignupForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']