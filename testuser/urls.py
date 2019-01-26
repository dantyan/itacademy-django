from django.urls import path

from testuser.views import users

app_name = 'testuser'
urlpatterns = [
    path('', users, name='home'),
]
