from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from geekshop.mixin import BaseClassContextMixin
from mainapp.models import ProductCategory, Product


# Create your views here.


class IndexTemplateView(TemplateView, BaseClassContextMixin):
    title = 'geekshop | main page'
    template_name = 'mainapp/index.html'


class ProductsListView(ListView, BaseClassContextMixin):
    model = Product
    paginate_by = 3
    title = 'geekshop | products'
    template_name = 'mainapp/products.html'
    context_object_name = 'products'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()

        if kwargs.get('category_id'):
            self.object_list = self.object_list.filter(category_id=kwargs['category_id'])

        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all().order_by('id')

        return context



# def index(request):
#     return render(request, 'mainapp/index.html', {'title': 'geekshop | main page'})


# def products(request, category_id=None, page_id=1):
#
#     products = Product.objects.filter(category_id=category_id).order_by('id') if category_id != None else Product.objects.all().order_by('id')
#
#     paginator = Paginator(products, per_page=3)
#
#     try:
#         products_paginator = paginator.page(page_id)
#     except PageNotAnInteger:
#         products_paginator = paginator.page(1)
#     except EmptyPage:
#         products_paginator = paginator.page(paginator.num_pages)
#
#     context = {'title': 'geekshop | products',
#                'categories': ProductCategory.objects.all().order_by('id'),
#                'products': products_paginator}
#     return render(request, 'mainapp/products.html', context)
#
