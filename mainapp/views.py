from django.shortcuts import render
from mainapp.models import ProductCategory, Product

# Create your views here.


def index(request):
    return render(request, 'mainapp/index.html', {'title': 'geekshop | main page'})


def products(request):
    context = {'title': 'geekshop | products',
               'carousel_items': [
                   {
                       'image': 'vendor/img/slides/slide-1.jpg',
                       'alt': 'First slide'
                   },
                   {
                       'image': 'vendor/img/slides/slide-2.jpg',
                       'alt': 'Second slide'
                   },
                   {
                       'image': 'vendor/img/slides/slide-3.jpg',
                       'alt': 'Third slide'
                   }
               ],
               'categories': ProductCategory.objects.all().order_by('id'),
               'products': Product.objects.all().order_by('id')}
    return render(request, 'mainapp/products.html', context)
