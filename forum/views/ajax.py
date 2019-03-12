from django.http import JsonResponse

from forum.models import Post


def ajax_view(request):
    post = Post.objects.order_by('?').first()

    return JsonResponse({
        'title': post.title,
        'id': post.pk,
        'content': post.content,
    })

# def ajax_view(request):
#     return HttpResponse('text response')

# def ajax_view(request):
#     return HttpResponse('<h1 class="text-right">H1 ajax response</h1>')

# def ajax_view(request):
#     post = Post.objects.order_by('?').first()
#     return render(request, 'pages/block/ajax-post.html', {
#         'post': post
#     })
