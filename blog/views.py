from django.shortcuts import redirect, render
from django.urls import reverse

from blog.forms import PostForm, ThemeForm
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


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect(reverse('blog:home'))
    else:
        form = PostForm()

    return render(request, 'articles/add-post.html', {
        'form': form
    })


def add_theme(request):
    if request.method == 'POST':
        form = ThemeForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)

            obj.user = request.user
            obj.save()

            return redirect(reverse('blog:home'))
    else:
        form = ThemeForm()

    return render(request, 'articles/add-theme.html', {
        'form': form
    })


def search_result(request):
    q = request.GET.get('q')
    search_option = request.GET.get('search_option')
    use_content = request.GET.get('content')

    if search_option == 'exact':
        posts = Post.objects.filter(title__iexact=q)
    elif search_option == 'starts_with':
        pass
    elif search_option == 'ends_with':
        pass
    else:
        posts = Post.objects.filter(title__icontains=q)

    # if use_content:
    #     posts = Post.objects.filter(
    #         Q(title__icontains=q) | Q(content__icontains=q)
    #     )
    # else:
    #     posts = Post.objects.filter(title__icontains=q)

    # query = [Q(title__icontains=q)]
    #
    # if use_content:
    #     query.append(Q(content__icontains=q))
    #
    # posts = Post.objects.filter(reduce(operator.or_, query))

    return render(request, 'articles/home.html', {
        'posts': posts,
        'q': q
    })
