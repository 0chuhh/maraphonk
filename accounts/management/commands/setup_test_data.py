import random

from django.db import transaction
from django.core.management.base import BaseCommand

from accounts.models import User
from charitable_organization.models import CharitableOrg
from inventory.models import Inventory
from marathon.models import Marathon
from accounts.factories import UserFactory
from charitable_organization.factories import CharitableOrgFactory
from inventory.factories import InventoryFactory
from marathon.factories import *
from sponsorship.factories import SponsorshipFactory

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        User.objects.filter(is_superuser=False).delete()
        # CharitableOrg.objects.all().delete()
        # Inventory.objects.all().delete()
        # Marathon.objects.all().delete()
        # Route.objects.all().delete()
        # Sponsorship.objects.all().delete()

        self.stdout.write("Creating new data...")
        people = []
        for _ in range(500):
            person = UserFactory()
            # people.append(person)
            # charitable_organization = CharitableOrgFactory()
            # inventory = InventoryOrgFactory()
            # marathon = MarathonFactory()
            # checkpoint = CheckpointFactory()
            # route = RouteFactory()
            # route_checkpoints = RouteCheckpointsFactory()
            # sponsorship = SponsorshipFactory()
            # runners = RunnersFactory()
        # print(User.objects.filter(groups__name='runner'))
