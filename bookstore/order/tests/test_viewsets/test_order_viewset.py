from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from order.models import Order
from product.models import Product, Category


class OrderViewSetTest(APITestCase):

    def setUp(self):
        self.client = APIClient()

        
        self.user = User.objects.create_user(
            username="rafael",
            password="123456"
        )

        
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        
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

        self.url = "/bookstore/v1/order/"