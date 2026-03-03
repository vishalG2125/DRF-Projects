from django.contrib import admin

from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'quantity', 'total_price', 'purchase_datetime')
    list_filter = ('purchase_datetime',)
