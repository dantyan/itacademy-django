from django.urls import path

from user.views import user_login

app_name = 'user'
urlpatterns = [
    path('login/', user_login, name='user-login'),
]
