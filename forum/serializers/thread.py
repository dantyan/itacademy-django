from rest_framework import serializers

from forum.models import Thread


class ThreadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thread
        fields = [
            'pk',
            'title',
            'description',
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
