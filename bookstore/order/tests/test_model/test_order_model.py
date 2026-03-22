from django.test import TestCase
from django.contrib.auth.models import User
from order.models import Order
from product.models import Product, Category

# Create your tests here.


class OrderModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="rafael",
            password="123456"
        )

        self.category = Category.objects.create(
            title="Eletrônicos",
            slug="eletronicos"
        )

        self.product1 = Product.objects.create(
            title="Notebook",
            price=5000
        )

        self.product2 = Product.objects.create(
            title="Mouse",
            price=100
        )

        self.product1.category.add(self.category)
        self.product2.category.add(self.category)

        self.order = Order.objects.create(user=self.user)

        self.order.product.add(self.product1, self.product2)

    def test_order_creation(self):
        self.assertEqual(self.order.user.username, "rafael")

    def test_order_products_relationship(self):
        self.assertEqual(self.order.product.count(), 2)
        self.assertIn(self.product1, self.order.product.all())
        self.assertIn(self.product2, self.order.product.all())

    def test_order_user_relationship(self):
        self.assertEqual(self.order.user, self.user)