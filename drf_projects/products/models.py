from django.conf import settings
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.PositiveIntegerField()
    vendor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'vendor'], name='unique_product_name_per_vendor')
        ]
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.vendor.username}'
