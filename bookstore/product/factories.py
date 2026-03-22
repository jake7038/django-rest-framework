import factory
from product.models import Product, Category


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    title = factory.Faker('word')
    slug = factory.Faker('slug')
    description = factory.Faker('sentence')
    active = factory.Iterator([True, False])


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Faker('word')
    price = factory.Faker('pyint')

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.category.add(category)
        else:
            category = CategoryFactory()
            self.category.add(category)