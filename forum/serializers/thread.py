from rest_framework import serializers

from forum.models import Thread
from forum.serializers.post import PostSerializer
from user.serializers.user import UserSerializer


class ThreadSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    post_set = PostSerializer(many=True)

    foo = serializers.SerializerMethodField()

    class Meta:
        model = Thread
        fields = [
            'pk',
            'title',
            'description',
            'add_time',
            'private',
            'post_cnt',
            'comment_cnt',

            'author',
            'foo',
            'post_set'
        ]

    def get_author(self, obj):
        return '{}:{}'.format(obj.author.id, obj.author)

    def get_foo(self, obj):
        return obj.post_set.count()


class LiteThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = [
            'pk',
            'title',
            'description',
        ]
