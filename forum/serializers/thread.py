from rest_framework import serializers

from forum.models import Thread


class ThreadSerializer(serializers.ModelSerializer):
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
        ]
