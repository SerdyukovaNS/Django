from django.test import TestCase

# Create your tests here.
from mainapp.models import Product, ProductCategories
from django.test.client import Client


class TestMainSmokeTest(TestCase):

    def setUp(self) -> None:
        category = ProductCategories.objects.create(name='test')
        Product.objects.create(category=category, name='product_1', price=100)
        self.client = Client()

    def test_product_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_product(self):
        for product_item in Product.objects.all():
            response = self.client.get(f'/products/detail/{product_item.pk}/')
            self.assertEqual(response.status_code, 200)

    def tearDown(self) -> None:
        pass
