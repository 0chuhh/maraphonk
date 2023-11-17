# For creating test data
import factory
from factory.django import DjangoModelFactory

from .models import CharitableOrg


class CharitableOrgFactory(DjangoModelFactory):
    class Meta:
        model = CharitableOrg

    name = factory.Faker("sentence")
