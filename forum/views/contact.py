from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from forum.forms import ContactForm


class ContactView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('forum:home')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
