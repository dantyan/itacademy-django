from django.db import models
from django.urls import reverse


class Thread(models.Model):

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(
        'user.UserModel',
        on_delete=models.SET_NULL,
        null=True,
    )
    add_time = models.DateTimeField(auto_now_add=True)
    private = models.BooleanField(default=False)

    post_cnt = models.IntegerField(default=0)
    comment_cnt = models.IntegerField(default=0)

    last_post_time = models.DateTimeField(
        null=True,
        blank=True,
        editable=False
    )
    last_comment_time = models.DateTimeField(
        null=True,
        blank=True,
        editable=False
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('forum:thread', kwargs={'pk': self.pk})
