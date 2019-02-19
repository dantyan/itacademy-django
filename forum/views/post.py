from django.db.models import F
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from forum.forms import CommentForm, PostForm
from forum.models import Comment, Post


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

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        # BAD
        # self.object.views_cnt += 1
        # update post set views_cnt = 1

        # GOOD
        self.object.views_cnt = F('views_cnt') + 1
        # update post set views_cnt = views_cnt + 1

        self.object.save()

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm(initial={'post': self.object})
        context['comments'] = Comment.objects.filter(post=self.object)
        return context
