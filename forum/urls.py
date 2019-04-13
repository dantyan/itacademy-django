from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers

from forum.views.ajax import ajax_view
from forum.views.chat import add_message, chat, messages
from forum.views.comment import CreateCommentView
from forum.views.contact import ContactView
from forum.views.home import HomeView
from forum.views.post import CreatePostView, PostView, UpdatePostView
from forum.views.reach import ReachView
from forum.views.thread import ThreadView
from forum.viewsets.post import PostViewSet
from forum.viewsets.thread import ThreadViewset

router = routers.SimpleRouter()
router.register('thread', ThreadViewset, )
router.register('post', PostViewSet, )

app_name = 'forum'
urlpatterns = [
    path('', HomeView.as_view(), name="home"),

    path('api/', include(router.urls)),

    path('thread/<int:pk>/', ThreadView.as_view(), name="thread"),

    path('about/', TemplateView.as_view(template_name='pages/about.html')),

    path('post/<int:pk>/', PostView.as_view(), name="post"),
    path('post/create/', CreatePostView.as_view(), name="create-post"),
    path('post/update/<int:pk>/', UpdatePostView.as_view(), name="update-post"),
    path('post/delete/<int:pk>/', UpdatePostView.as_view(), name="delete-post"),

    path('comment/create/', CreateCommentView.as_view(), name="create-comment"),

    path('contact/', ContactView.as_view()),

    path('ajaxReachView/', ajax_view, name="ajax"),

    # chat ---
    path('chat/', chat, name="chat"),
    path('chat/messages/', messages, name="chat-messages"),
    path('chat/add/', add_message, name="chat-add"),

    path('reach/', ReachView.as_view()),
]
