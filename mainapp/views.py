from django.shortcuts import render
from os.path import dirname
import json

# Create your views here.


def index(request):
    return render(request, 'mainapp/index.html', {'title': 'geekshop | main page'})


def products(request):
    context = dict()
    with open(dirname(__file__) + '/fixtures/products.json') as c:
        for item in json.load(c):
            context.update(item)
    return render(request, 'mainapp/products.html', context)
