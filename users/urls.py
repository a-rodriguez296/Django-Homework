from django.conf.urls import include, url
from django.contrib import admin
from users.views import LoginView, LogOutView, SignupView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    #Este es el redireccionamiento de la parte de users
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogOutView.as_view(), name='users_logout'),
    url(r'^signup$', SignupView.as_view(), name='users_signup'),
]


