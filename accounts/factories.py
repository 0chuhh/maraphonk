# For creating test data
import factory
from factory.django import DjangoModelFactory

from .models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    print(factory.Faker("username"))

    username = factory.Sequence(lambda n: "user_%d" % n)
    first_name = factory.Faker("first_name")
    middle_name = factory.Faker("first_name")
    last_name = factory.Faker("first_name")
