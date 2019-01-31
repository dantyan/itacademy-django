from django.db.models import Q
from django.shortcuts import render

from testuser.models import TestUser


def users(request):
    testusers = TestUser.objects.filter(
        username__icontains='fose',
        username__contains='maria',
        is_active=True
    ).exclude(
        Q(username__istartswith='maria') | Q(username__iendswith='maria')
    ).order_by('-id')

    print(testusers.query)

    testusers = TestUser.objects.filter(
        Q(username__icontains='maria') | Q(username__icontains='fose'),
        is_active=True
    ).order_by('-id')

    return render(request, 'maria/home.html', {
        'users': testusers
    })
