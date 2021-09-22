from django.shortcuts import render

# Create your views here.
from users.forms import UserLoginForm


def login(request):
    form = UserLoginForm()
    context = {
        'title': 'geekshop | авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)


def register(request):
    context = {
        'title': 'geekshop | регистрация'
    }
    return render(request, 'users/register.html', context)
