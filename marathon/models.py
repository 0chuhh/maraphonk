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
    country = models.CharField(max_length=255,default="Russia")

    def __str__(self):
        return self.name


class Checkpoint(models.Model):
    name = models.CharField(
        max_length=255
    )
    position = models.CharField(
        max_length=255
    )

    def __str__(self):
        return self.name


class Route(models.Model):
    name = models.CharField(
        max_length=255
    )
    location = models.CharField(
        max_length=255
    )
    map = models.ImageField(upload_to="media/images")

    def __str__(self):
        return self.name


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

    def __str__(self):
        return f"{self.route.name} {self.distance_from_start}km"


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

    def __str__(self):
        return f"{self.user.name} {self.marathon.name}"