from django.db import models


class Inventory(models.Model):
    name = models.CharField(
        max_length=255
    )
    count = models.IntegerField()
    need_to_order = models.IntegerField()