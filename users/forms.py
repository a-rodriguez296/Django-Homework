#-*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    usr = forms.CharField(label="Nombre de usuario")
    pwd = forms.CharField(label="Contraseña", widget=forms.PasswordInput())


class SignupForm(forms.ModelForm):

    def save(self, commit=True):
        #Este metodo crea la instancia de user, pero como tiene el commit en False, no la guarda en DB
        user = super(SignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput()
        }