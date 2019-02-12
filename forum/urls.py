from django.urls import path
from django.views.generic import TemplateView

from forum.views import HomeView, ThreadView

app_name = 'forum'
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('thread/<int:pk>/', ThreadView.as_view(), name="thread"),
    path('about/', TemplateView.as_view(template_name='pages/about.html')),
]
