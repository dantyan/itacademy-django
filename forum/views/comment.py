from django.urls import reverse
from django.views.generic import CreateView

from forum.forms import CommentForm
from forum.models import Comment


class CreateCommentView(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('forum:post', kwargs={'pk': self.object.post_id})
