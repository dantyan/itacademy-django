from django.contrib.auth import views as auth_views
from django.shortcuts import render


def home(request):
    return render(request, 'profile/home.html')


class LoginView(auth_views.LoginView):
    template_name = 'profile/login.html'
