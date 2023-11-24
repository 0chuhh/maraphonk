# For creating test data
import random
import factory
from django.core.files.base import ContentFile
from factory.django import DjangoModelFactory
from sponsorship.models import Sponsorship
from accounts.models import User
from .models import *


class MarathonFactory(DjangoModelFactory):
    class Meta:
        model = Marathon

    name = factory.Faker("sentence")
    description = factory.Faker("sentence")
    country = factory.Faker("country")


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


class RouteCheckpointsFactory(DjangoModelFactory):
    class Meta:
        model = RouteCheckpoint

    route = factory.SubFactory(RouteFactory)
    checkpoint = factory.SubFactory(CheckpointFactory)
    distance_from_start = factory.LazyAttribute(lambda x: random.randrange(1,20))


class SponsorshipFactory(DjangoModelFactory):
    class Meta:
        model = Sponsorship

