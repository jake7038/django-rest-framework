import factory
from django.contrib.auth.models import User
from product.factories import ProductFactory

from product.models import Product
from product.models import Category

class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('pystr')
    slug = factory.Faker('pystr')
    descripton = factory.Faker('pystr')
    active = factory.Iterator([True, False])
    
    class Meta:
        model = Category
class ProductFactor(factory.django.DjangoModelFactory):
    price = factory.Faker('pyint')
    category = factory.LazyAttribute(CategoryFactory)
    title = factory.Faker('pystr')

    @factory.post_generation
    def category(self, create, extracted, **kwaregs):
        if not create:
            return
        
        if extracted:
            for category in extracted:
                self.category.add(category)
    class Meta:
        model = Product