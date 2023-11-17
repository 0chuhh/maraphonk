# For creating test data
import random
import factory
from factory.django import DjangoModelFactory

from .models import Inventory


class InventoryOrgFactory(DjangoModelFactory):
    class Meta:
        model = Inventory

    name = factory.Faker("sentence")
    count = factory.LazyAttribute(lambda x: random.randrange(0, 10000))
    need_to_order = factory.LazyAttribute(lambda x: random.randrange(0, 10000))
