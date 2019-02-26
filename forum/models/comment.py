from django.db import models


class Comment(models.Model):
    user = models.ForeignKey(
        'user.UserModel',
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        'forum.Post',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.TextField()
    add_time = models.DateTimeField(
        auto_now_add=True
    )
