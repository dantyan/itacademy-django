from django.utils.translation import (
    ngettext,
    ugettext,
)
from django.views.generic import TemplateView

from forum.models import Thread


# from django.utils.translation import ugettext as _


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        data['threads'] = Thread.objects.all()

        data['title'] = ugettext('Forum Home')
        data['subtitle'] = ugettext('Forum subtitle {}').format('BURUM')

        data['messages'] = ngettext('message', 'messages', 1)
        data['messages_plural'] = ngettext('message', 'messages', 10)

        return data
