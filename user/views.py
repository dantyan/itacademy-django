from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render


# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AuthenticationForm()

    return render(request, 'profile/login.html', {
        'form': form,
    })
