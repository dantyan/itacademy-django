from django.urls import path

from blog.views import add_post, add_theme, home, post, theme

app_name = 'blog'
urlpatterns = [
    path('', home, name='home'),
    path('post-<int:pk>/', post, name="post"),
    path('theme-<int:pk>/', theme, name="theme"),

    path('add/', add_post, name="add"),
    path('add-theme', add_theme, name='add-theme')
]
