from django.db import models
from django.conf import settings
from charitable_organization.models import CharitableOrg
from inventory.models import Inventory


class Marathon(models.Model):
    name = models.CharField(
        max_length=255
    )
    description = models.CharField(
        max_length=255
    )


class Checkpoint(models.Model):
    name = models.CharField(
        max_length=255
    )
    position = models.CharField(
        max_length=255
    )


class Route(models.Model):
    name = models.CharField(
        max_length=255
    )
    location = models.CharField(
        max_length=255
    )
    map = models.ImageField(upload_to="media/images")


class RouteCheckpoint(models.Model):
    route = models.ForeignKey(
        Route,
        on_delete=models.CASCADE
    )
    checkpoint = models.ForeignKey(
        Checkpoint,
        on_delete=models.CASCADE
    )
    distance_from_start = models.FloatField()


class Runners(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    marathon = models.ForeignKey(
        Marathon,
        on_delete=models.CASCADE
    )
    charitable_organization = models.ForeignKey(
        CharitableOrg,
        on_delete=models.CASCADE
    )
    inventory_item = models.ForeignKey(
        Inventory,
        on_delete=models.CASCADE
    )
    route = models.ForeignKey(
        Route,
        on_delete=models.CASCADE
    )
