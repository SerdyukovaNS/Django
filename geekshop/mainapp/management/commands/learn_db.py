import json
from chardet import detect
from django.core.management.base import BaseCommand
from django.db.models import Q
from mainapp.models import ProductCategories, Product
from authapp.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        # product = Product.objects.filter(
        #     Q(category__name='Обувь') | Q(id=5)
        # )

        # product = Product.objects.filter(
        #     Q(category__name='Обувь') & Q(id=5)
        # )

        # product = Product.objects.filter(
        #     ~Q(category__name='Обувь')
        # )

        product = Product.objects.filter(
            Q(category__name='Обувь'), id=5
        )

        print(product)
