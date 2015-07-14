#-*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.generic import View
from users.forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login as django_login, logout as django_logout

class SignupView(View):

    def get(self, request):
        form = SignupForm()
        context = {
            'signup_form': form
        }
        return render(request, 'users/signup.html', context)

    def post(self, request):
        error_messages = []
        form = SignupForm(request.POST)

        if form.is_valid():

            #Guardar el usuario nuevo
            new_user = form.save()

            #Poner los campos en blanco
            form = SignupForm()

            return redirect('posts_home')
        else:

            #Pregunta. En el html pq no me pinta los campos de nuevo
            form = SignupForm()
            context = {
                'form': form,
                'message': 'Hay errores en el formulario. Intenta de nuevo.'
            }
            return render(request, 'users/signup.html', context)





class LoginView(View):
    def get(self, request):
        error_messages = []
        form = LoginForm()
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)

    def post(self, request):
        error_messages = []

        form = LoginForm(request.POST)

        #con esto se valida que los datos cumplan con lo que se especifica en el modelo
        if form.is_valid():

            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')

            user = authenticate(username=username, password=password)

            if user is None:
                error_messages.append('Nombre de usuario o contraseña incorrecta')
            else:
                if user.is_active:
                    django_login(request, user)
                    return redirect('posts_home')
                else:
                    error_messages.append('El usuario no está activo')
            context = {
                'errors': error_messages,
                'login_form': form
            }
            return render(request, 'users/login.html', context)


class LogOutView(View):

    def get(self, request):
        if request.user.is_authenticated():
            django_logout(request)
            return redirect('posts_home')