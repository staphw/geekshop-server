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
        data_json = load_from_json('data')

        for item in data_json:
            if item.get('categories'):
                ProductCategory.objects.all().delete()
                for category in item.get('categories'):
                    new_category = ProductCategory(**category)
                    new_category.save()

            if item.get('products'):
                Product.objects.all().delete()
                for product in item.get('products'):
                    category_name = product['category']
                    category = ProductCategory.objects.get(name=category_name)
                    product['category'] = category
                    new_product = Product(**product)
                    new_product.save()

            if item.get('slides'):
                Slide.objects.all().delete()
                for slide in item.get('slides'):
                    new_slide = Slide(**slide)
                    new_slide.save()

        # super_user = User.objects.create_superuser('administrator', '', 'adm')
