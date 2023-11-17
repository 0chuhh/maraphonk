from django.db import models


class Inventory(models.Model):
    name = models.CharField(
        max_length=255
    )
    count = models.IntegerField()
    need_to_order = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.name}'

