from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    vendor_username = serializers.CharField(source='vendor.username', read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'stock',
            'vendor',
            'vendor_username',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('vendor', 'created_at', 'updated_at')

    def validate(self, attrs):
        request = self.context.get('request')
        vendor = attrs.get('vendor') or getattr(self.instance, 'vendor', None) or getattr(request, 'user', None)
        name = attrs.get('name') or getattr(self.instance, 'name', None)

        if vendor and name:
            query = Product.objects.filter(vendor=vendor, name__iexact=name)
            if self.instance:
                query = query.exclude(pk=self.instance.pk)
            if query.exists():
                raise serializers.ValidationError('Duplicate product for this vendor is not allowed.')
        return attrs
