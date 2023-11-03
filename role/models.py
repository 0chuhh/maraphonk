from django.db import models
from django.conf import settings


class Role(models.Model):
    name = models.CharField(max_length=255)


class UserRole(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
    )

