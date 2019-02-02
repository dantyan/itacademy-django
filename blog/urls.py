from django.urls import path

from blog.views import add_post, add_theme, home, post, search_result, theme

app_name = 'blog'
urlpatterns = [
    path('', home, name='home'),
    path('post-<int:pk>/', post, name="post"),
    path('theme-<int:pk>/', theme, name="theme"),

    path('search-result/', search_result, name='search-result'),

    path('add/', add_post, name="add"),
    path('add-theme', add_theme, name='add-theme')
]
