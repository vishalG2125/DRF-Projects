from rest_framework import serializers

from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    customer_username = serializers.CharField(source='customer.username', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'customer',
            'customer_username',
            'product',
            'product_name',
            'quantity',
            'total_price',
            'purchase_datetime',
        )
        read_only_fields = ('total_price', 'purchase_datetime', 'customer')

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError('Quantity must be greater than zero.')
        return value

    def validate(self, attrs):
        product = attrs.get('product') or getattr(self.instance, 'product', None)
        quantity = attrs.get('quantity') or getattr(self.instance, 'quantity', 0)

        if product and quantity and product.stock < quantity:
            raise serializers.ValidationError('Insufficient product stock.')
        return attrs
