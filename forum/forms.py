from django import forms
from django.forms import widgets

from forum.models import Post, Comment


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
