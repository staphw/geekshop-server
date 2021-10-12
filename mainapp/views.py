from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from mainapp.models import ProductCategory, Product

# Create your views here.


def index(request):
    return render(request, 'mainapp/index.html', {'title': 'geekshop | main page'})


def products(request, category_id=None, page_id=1):

    products = Product.objects.filter(category_id=category_id).order_by('id') if category_id != None else Product.objects.all().order_by('id')

    paginator = Paginator(products, per_page=3)

    try:
        products_paginator = paginator.page(page_id)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {'title': 'geekshop | products',
               'categories': ProductCategory.objects.all().order_by('id'),
               'products': products_paginator}
    return render(request, 'mainapp/products.html', context)
