from django.views.generic import TemplateView

from forum.models import Thread


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        data['threads'] = Thread.objects.all()
        return data
