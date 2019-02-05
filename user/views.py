from django.contrib.auth import views as auth_views
from django.shortcuts import redirect, render


def home(request):
    return render(request, 'profile/home.html')


def logout(request):
    request.session.flush()
    return redirect('/user/')


class LoginView(auth_views.LoginView):
    template_name = 'profile/login.html'

# class LogoutView(auth_views.LogoutView):
#     template_name = 'user/logout.html'
