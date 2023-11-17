from django.db import models


class CharitableOrg(models.Model):
    name = models.CharField(
        max_length=255
    )

    def __str__(self):
        return f'{self.id} - {self.name}'

