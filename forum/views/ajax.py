from datetime import datetime

from django.http import JsonResponse

from forum.forms import CommentForm


def ajax_view(request):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()

    return JsonResponse({
        "comment": '{} - {}'.format(datetime.now(), comment.content),
        'pk': comment.pk
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
