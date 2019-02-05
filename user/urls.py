from django.urls import path

from user.views import LoginView, home

app_name = 'user'
urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(), name='user-login'),
]
