# For creating test data
import factory
from factory.django import DjangoModelFactory
from django.contrib.auth.models import Group
from .models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    with factory.Faker.override_default_locale('ru_RU'):
        email = factory.Faker('email')
        username = factory.Faker('email')
        first_name = factory.Faker("first_name")
        middle_name = factory.Faker("first_name")
        last_name = factory.Faker("first_name")
        country = factory.Faker("country")
        factory.PostGenerationMethodCall('set_password', 'adm1n')
