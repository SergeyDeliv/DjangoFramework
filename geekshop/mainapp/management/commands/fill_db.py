import json
import os

from django.conf import settings
from django.core.management import BaseCommand

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product

JSON_PATH = 'mainapp/json/'


def loadFromJSON(file_name):
    with open(os.path.join(settings.BASE_DIR, f'mainapp/json/{file_name}.json'), encoding='UTF-8') as f:
        return json.load(f)


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        categories = loadFromJSON('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = loadFromJSON('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product['category']
            # Получаем категорию по имени
            _category = ProductCategory.objects.get(name=category_name)
            # Заменяем название категории объектом
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

        # Создаём суперпользователя
        ShopUser.objects.create_superuser('django', 'django@local.gb', 'geekbrains', age=30)
