from django.db import models
from django.conf import settings
from marathon.models import Marathon


class Sponsorship(models.Model):
    sponsor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sponsor'
    )
    runner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='runner'
    )
    marathon = models.ForeignKey(
        Marathon,
        on_delete=models.CASCADE
    )
    sum = models.DecimalField(
        max_digits=10,
        decimal_places=6
    )
