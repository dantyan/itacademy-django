from django.shortcuts import render

from blog.models import Post


def home(request):
    posts = Post.objects.all()

    return render(request, 'articles/home.html', {
        'posts': posts
    })


def post(request, pk):
    blog_post = Post.objects.get(id=pk)

    return render(request, 'articles/post.html', {
        'post': blog_post
    })
