from django.views.generic import DetailView

from forum.models import Thread, Post


class ThreadView(DetailView):
    template_name = 'pages/thread.html'
    model = Thread

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['children'] = Thread.objects.filter(parent=self.object)
        context['posts'] = Post.objects.filter(thread=self.object)

        return context
