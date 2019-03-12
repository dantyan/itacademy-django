from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models
from django.urls import reverse


class Post(models.Model):
    thread = models.ForeignKey(
        'forum.Thread',
        on_delete=models.CASCADE,
        null=True,
        help_text='Some usefull help text'
    )
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

    tags_list = ArrayField(
        models.CharField(max_length=10),
        default=list
    )
    options = JSONField(
        default=dict
    )

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('forum:post', kwargs={'pk': self.pk})
