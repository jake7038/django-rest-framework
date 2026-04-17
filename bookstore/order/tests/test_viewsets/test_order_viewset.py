from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

from order.models import Order
from product.models import Product, Category


class OrderViewSetTest(APITestCase):

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

        self.url = "/bookstore/v1/order/"

    def test_create_order(self):
        data = {
            "user": self.user.id,
            "products_id": [self.product1.id, self.product2.id]
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)

        order = Order.objects.first()
        self.assertEqual(order.product.count(), 2)

    def test_list_orders(self):
        order = Order.objects.create(user=self.user)
        order.product.add(self.product1)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_order(self):
        order = Order.objects.create(user=self.user)
        order.product.add(self.product1)

        url = f"/bookstore/v1/order/{order.id}/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["total"], self.product1.price)

    def test_delete_order(self):
        order = Order.objects.create(user=self.user)

        url = f"/bookstore/v1/order/{order.id}/"
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Order.objects.count(), 0)