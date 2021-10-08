from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from mainapp.models import ProductCategory, Product, Slide

import json, os

JSON_PATH = 'mainapp/fixtures'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('productcategory')

        ProductCategory.objects.all().delete()
        for category in categories:
            cat = category.get('fields')
            cat['id'] = category.get('pk')
            new_category = ProductCategory(**cat)
            new_category.save()

        products = load_from_json('product')

        Product.objects.all().delete()
        for product in products:
            prod = product.get('fields')
            prod['id'] = product.get('pk')
            category_id = prod.get('category')
            category = ProductCategory.objects.get(id=category_id)
            prod['category'] = category
            new_product = Product(**prod)
            new_product.save()

    super_user = User.objects.create_superuser('admin', '', 'admin')
