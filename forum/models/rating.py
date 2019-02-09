from django.db import models


class Rating(models.Model):
    user = models.ForeignKey(
        'user.UserModel',
        on_delete=models.CASCADE,
        related_name='+'
    )
    post = models.ForeignKey(
        'forum.Post',
        on_delete=models.CASCADE,
        related_name='+'
    )
    add_time = models.DateTimeField(auto_now_add=True)
    mark = models.PositiveSmallIntegerField()
