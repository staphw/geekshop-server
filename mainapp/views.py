from django.shortcuts import render
from mainapp.models import ProductCategory, Product

# Create your views here.


def index(request):
    return render(request, 'mainapp/index.html', {'title': 'geekshop | main page'})


def products(request):
    context = {'title': 'geekshop | products',
               'categories': ProductCategory.objects.all().order_by('id'),
               'products': Product.objects.all().order_by('id')}
    return render(request, 'mainapp/products.html', context)
