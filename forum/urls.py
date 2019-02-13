from django.urls import path
from django.views.generic import TemplateView, CreateView

from forum.views.comment import CreateCommentView
from forum.views.home import HomeView
from forum.views.post import PostView, CreatePostView, UpdatePostView
from forum.views.thread import ThreadView

app_name = 'forum'
urlpatterns = [
    path('', HomeView.as_view(), name="home"),

    path('thread/<int:pk>/', ThreadView.as_view(), name="thread"),

    path('about/', TemplateView.as_view(template_name='pages/about.html')),

    path('post/<int:pk>/', PostView.as_view(), name="post"),
    path('post/create/', CreatePostView.as_view(), name="create-post"),
    path('post/update/<int:pk>/', UpdatePostView.as_view(), name="update-post"),
    path('post/delete/<int:pk>/', UpdatePostView.as_view(), name="delete-post"),

    path('comment/create/', CreateCommentView.as_view(), name="create-comment"),
]
