from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.generic import TemplateView

from forum.models import Thread


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        data['threads'] = Thread.objects.all()

        send_mail(
            subject='Mail subject',
            message='Hello from forum',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['dan.tyan@gmail.com'],
            html_message=render_to_string(
                'email/test-mail.html',
                {
                    'foo': 'Cool forum',
                    'bar': 100
                }
            )
        )

        return data
