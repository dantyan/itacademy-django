from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from forum.models import Chat


def chat(request):
    _messages = Chat.objects.all()
    return render(request, 'chat/home.html', {
        'messages': _messages
    })


def messages(request):
    return render(request, 'chat/home.html', {})


@require_POST
@login_required
def add_message(request):
    message_text = request.POST.get('message')
    if message_text:
        _message = Chat.objects.create(
            message=message_text,
            user=request.user,
        )
        return JsonResponse({
            'message': _message.message,
            'user': _message.user_id,
        })

    return JsonResponse({
        'error': 'empty message',
    })
