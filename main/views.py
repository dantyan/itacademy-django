from django.shortcuts import render


def index(request):
    fruits = ['Apple', 'Banana', 'Cherry']

    return render(request, 'burum/index.html', {
        'fruits': fruits,
    })
