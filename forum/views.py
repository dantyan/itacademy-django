from django.views.generic import DetailView, TemplateView

from forum.models import Thread


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        data['threads'] = Thread.objects.all()

        return data


class ThreadView(DetailView):
    template_name = 'pages/thread.html'
    model = Thread
