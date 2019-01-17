from django.shortcuts import render

from blog.models import Post, Theme


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


def theme(request, pk):
    blog_theme = Theme.objects.get(id=pk)
    posts = Post.objects.filter(theme=blog_theme)

    return render(request, 'articles/home.html', {
        'posts': posts
    })
