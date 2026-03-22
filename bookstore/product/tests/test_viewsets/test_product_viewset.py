from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token 
from product.models import Product, Category
from order.factories import UserFactory

class ProductViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.token = Token.objects.create(user=self.user)

        # 🔥 AUTENTICAÇÃO AQUI
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.category1 = Category.objects.create(
            title="Eletrônicos",
            slug="eletronicos"
        )

        self.category2 = Category.objects.create(
            title="Acessórios",
            slug="acessorios"
        )

        self.url = "/bookstore/v1/product/"

    def test_create_product(self):
        data = {
            "title": "Notebook",
            "description": "Notebook potente",
            "price": 5000,
            "active": True,
            "categories_id": [self.category1.id, self.category2.id]
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)

        product = Product.objects.first()
        self.assertEqual(product.title, "Notebook")
        self.assertEqual(product.category.count(), 2)

    def test_list_products(self):
        product = Product.objects.create(
            title="Mouse",
            price=100
        )
        product.category.add(self.category1)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_retrieve_product(self):
        product = Product.objects.create(
            title="Teclado",
            price=200
        )
        product.category.add(self.category1)

        url = f"/bookstore/v1/product/{product.id}/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Teclado")

    def test_delete_product(self):
        product = Product.objects.create(
            title="Monitor",
            price=800
        )

        url = f"/bookstore/v1/product/{product.id}/"
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)