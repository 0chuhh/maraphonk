# For creating test data
import random
import factory
from django.core.files.base import ContentFile
from factory.django import DjangoModelFactory

from .models import *


class MarathonFactory(DjangoModelFactory):
    class Meta:
        model = Marathon

    name = factory.Faker("sentence")
    description = factory.Faker("sentence")


class CheckpointFactory(DjangoModelFactory):
    class Meta:
        model = Checkpoint

    name = factory.Faker("sentence")
    position = factory.LazyAttribute(lambda x: f"широта:  {random.randrange(0, 100)}°{random.randrange(0, 100)}'{random.randrange(0, 100)}.{random.randrange(0, 100)}'N, долгота: {random.randrange(0, 100)}°{random.randrange(0, 100)}'{random.randrange(0, 100)}.{random.randrange(0, 100)}'W")


class RouteFactory(DjangoModelFactory):
    class Meta:
        model = Route

    name = factory.Faker("sentence")
    location = factory.LazyAttribute(lambda x: f"широта:  {random.randrange(0, 100)}°{random.randrange(0, 100)}'{random.randrange(0, 100)}.{random.randrange(0, 100)}'N, долгота: {random.randrange(0, 100)}°{random.randrange(0, 100)}'{random.randrange(0, 100)}.{random.randrange(0, 100)}'W")
    map = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data(
                {'width': 1024, 'height': 768}
            ), 'example.jpg'
        )
    )