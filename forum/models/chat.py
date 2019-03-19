from django.db import models


class Chat(models.Model):
    message = models.CharField(max_length=255)
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        'user.UserModel',
        on_delete=models.CASCADE,
        related_name='+'
    )

    class Meta:
        ordering = ['pk']
