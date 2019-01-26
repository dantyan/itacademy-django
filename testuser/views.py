from django.shortcuts import render

from testuser.models import TestUser


def users(request):
    testusers = TestUser.objects.all()

    return render(request, 'testuser/home.html')
