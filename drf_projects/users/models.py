from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        CUSTOMER = 'CUSTOMER', 'Customer'
        VENDOR = 'VENDOR', 'Vendor'

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=Role.choices)

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = self.Role.ADMIN
        super().save(*args, **kwargs)
