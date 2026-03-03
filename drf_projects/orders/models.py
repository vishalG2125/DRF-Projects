from decimal import Decimal

from django.conf import settings
from django.db import models

from products.models import Product


class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='orders')
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=14, decimal_places=2)
    purchase_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-purchase_datetime']

    def save(self, *args, **kwargs):
        self.total_price = Decimal(self.quantity) * self.product.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Order {self.pk} by {self.customer.username}'
