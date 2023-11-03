from django.db import models


class CharitableOrg(models.Model):
    name = models.CharField(
        max_length=255
    )
