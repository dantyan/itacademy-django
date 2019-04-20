from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from forum.filters import ThreadFilter
from forum.models import Thread
from forum.serializers.thread import LiteThreadSerializer, ThreadSerializer


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.author_id


class ThreadViewset(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    filter_class = ThreadFilter
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(author=self.request.user)
    #     return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return LiteThreadSerializer
        return self.serializer_class

    @action(
        detail=False,
        url_name='mine',
        url_path='favs',
        methods=['get', 'post']
    )
    def my_favorite(self, request):
        """
        My favs description
        :param request:
        :return:
        """
        print('my favorite')
        queryset = self.get_queryset()
        queryset = queryset.filter(pk=1)
        return Response(LiteThreadSerializer(queryset, many=True).data)
