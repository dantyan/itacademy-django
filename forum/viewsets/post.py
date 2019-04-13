from rest_framework import viewsets

from forum.filters import PostFilter
from forum.models import Post
from forum.serializers.post import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_class = PostFilter
