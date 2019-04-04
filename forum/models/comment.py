from django.db import models
from django.utils.translation import ugettext_lazy as _


class Comment(models.Model):
    user = models.ForeignKey(
        'user.UserModel',
        on_delete=models.CASCADE,
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

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return self.content

    def get_content(self):
        return self.content

    def save(self, *args, **kwargs):
        self.content = self.content.replace('<script>', '')

        super().save(*args, **kwargs)
    #
    #     self.post.comment_cnt = self.post.comments.count()
    #     self.post.save()
    #
    # def delete(self, using=None, keep_parents=False):
    #     self.status = 'deleted'
    #     self.save()
    #
