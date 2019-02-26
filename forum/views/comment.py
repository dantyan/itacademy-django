from django.urls import reverse
from django.views.generic import CreateView

from forum.forms import CommentForm
from forum.models import Comment


class CreateCommentView(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.user = self.request.user

        response = super().form_valid(form)

        count = Comment.objects.filter(post=self.object.post).count()
        # self.object.post.comment_cnt = F('comment_cnt') + 1
        self.object.post.comment_cnt = count
        self.object.post.save()

        return response

    def get_success_url(self):
        return reverse('forum:post', kwargs={'pk': self.object.post_id})
