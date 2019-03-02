from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.forms import widgets
from django.template.loader import render_to_string

from forum.models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['thread', 'title', 'content']
        widgets = {
            'thread': widgets.Select(attrs={
                'class': 'form-control'
            }),
            'title': widgets.TextInput(attrs={
                'class': 'form-control'
            }),
            'content': widgets.Textarea(attrs={
                'class': 'form-control'
            }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'content']
        widgets = {
            'post': widgets.HiddenInput(),
            'content': widgets.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
            }),
        }


class ContactForm(forms.Form):
    name = forms.CharField()
    subject = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4})
    )

    def send_email(self):
        cd = self.cleaned_data

        send_mail(
            subject=cd.get('subject'),
            message=render_to_string(
                'email/contact.html',
                {
                    'name': cd.get('name'),
                    'message': cd.get('message'),
                    'email': cd.get('email')
                }
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['dan.tyan@gmailcom'],
            fail_silently=True
        )
