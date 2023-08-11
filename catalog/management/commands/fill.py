from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()

        product_list = [
            {
                "name": "Продукт 1",
                "description": "первый",
                # "category": '1',
                "price": 111.22
            },
            {
                "name": "Продукт 2",
                "description": "второй",
                # "category": 2,
                "price": 222.33
            },
            {
                "name": "продукт 3",
                "description": "третий",
                # "category": 2,
                "price": 333.33
            }
        ]

        prod = []
        for item in product_list:
            prod.append(Product(**item))

        Product.objects.bulk_create(prod)