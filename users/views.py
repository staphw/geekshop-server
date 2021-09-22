from django.shortcuts import render

# Create your views here.


def login(request):
    context = {
        'title': 'geekshop | авторизация'
    }
    return render(request, 'users/login.html', context)


def register(request):
    context = {
        'title': 'geekshop | регистрация'
    }
    return render(request, 'users/register.html', context)
