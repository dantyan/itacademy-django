from django.http import JsonResponse

from forum.models import Post


def ajax_view(request):
    post = Post.objects.order_by('?').first()

    return JsonResponse({
        'title': post.title,
        'id': post.pk,
    })
