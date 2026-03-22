from django.test import TestCase
from product.models import Product, Category

# Create your tests here.

class ProductModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            title="Eletrônicos",
            slug="eletronicos"
        )

        
        self.product = Product.objects.create(
            title="Notebook",
            description="Notebook potente",
            price=5000,
            active=True
        )

        self.product.category.add(self.category)

    def test_product_creation(self):
        self.assertEqual(self.product.title, "Notebook")
        self.assertEqual(self.product.price, 5000)
        self.assertTrue(self.product.active)

    def test_product_category_relationship(self):
        self.assertEqual(self.product.category.count(), 1)
        self.assertEqual(self.product.category.first().title, "Eletrônicos")

    def test_product_str(self):
        self.assertEqual(str(self.product), self.product.title)


class CategoryModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            title="Livros",
            slug="livros"
        )

    def test_category_creation(self):
        self.assertEqual(self.category.title, "Livros")
        self.assertEqual(self.category.slug, "livros")

    def test_category_str(self):
        self.assertEqual(str(self.category), "Livros")