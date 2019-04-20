from time import sleep

from django.http import HttpResponse


def some_func(*args, **kwargs):
    print('some_func')
    sleep(20)
    return 'bar'


def mock_request(request):
    print('mock_request')

    price = 150
    bonus = 50
    amount = price - bonus
    res = some_func(amount, 12, 2)
    print(res)
    print('after some func')
    return HttpResponse({})
