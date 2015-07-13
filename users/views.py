from django.shortcuts import render
from django.views.generic import View
from users.forms import LoginForm


class LoginView(View):

    def get(self, request):

        error_messages = []
        form = LoginForm()
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)