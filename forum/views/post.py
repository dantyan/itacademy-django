from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from forum.forms import PostForm, CommentForm
from forum.models import Post, Comment


class CreatePostView(CreateView):
    model = Post
    template_name = 'pages/post/form.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'pages/post/form.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'pages/post/form.html'


class PostView(DetailView):
    model = Post
    template_name = 'pages/post/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm(initial={'post': self.object})
        context['comments'] = Comment.objects.filter(post=self.object)
        return context
