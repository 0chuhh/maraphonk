
import random
import factory
from django.core.files.base import ContentFile
from factory.django import DjangoModelFactory
from accounts.models import User
from marathon.factories import MarathonFactory
from accounts.factories import UserFactory
from .models import *


class SponsorshipFactory(DjangoModelFactory):
    class Meta:
        model = Sponsorship

    sponsor = User.objects.filter(groups__name='sponsor')[random.randrange(0,10)]
    runner = User.objects.filter(groups__name='runner')[random.randrange(0,10)]

    marathon = factory.SubFactory(MarathonFactory)
    sum = 1000


