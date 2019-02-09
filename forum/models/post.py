from django.db import models


class Post(models.Model):
    user = models.ForeignKey(
        'user.UserModel',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    content = models.TextField()

    add_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField('forum.Tag', blank=True)

    rating = models.FloatField(
        null=True,
    )

    views_cnt = models.IntegerField(default=0)
    comment_cnt = models.IntegerField(default=0)

    def __str__(self):
        return self.title
