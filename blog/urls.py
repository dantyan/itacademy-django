from django.urls import path

from blog.views import home, post

app_name = 'blog'
urlpatterns = [
    path('', home, name='home'),
    path('<int:pk>/', post, name="post")
]
