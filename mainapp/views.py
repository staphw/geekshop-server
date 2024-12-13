from django.shortcuts import render
from mainapp.models import ProductCategory, Product

# Create your views here.


def index(request):
    return render(request, 'mainapp/index.html', {'title': 'geekshop | main page'})


def products(request, category_id=None):
    if category_id:
        products = Product.objects.filter(category_id=category_id).order_by('id')
    else:
        products = Product.objects.all().order_by('id')
    context = {'title': 'geekshop | products',
               'categories': ProductCategory.objects.all().order_by('id'),
               'products': products}
    return render(request, 'mainapp/products.html', context)
