from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
