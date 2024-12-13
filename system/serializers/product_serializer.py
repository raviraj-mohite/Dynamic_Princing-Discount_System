from rest_framework import serializers
from ..models.product import Product,SeasonalProduct, BulkProduct, PremiumProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'base_price']

class SeasonalProductSerializer(ProductSerializer):
    class Meta(ProductSerializer.Meta):
        model = SeasonalProduct

class BulkProductSerializer(ProductSerializer):
    class Meta(ProductSerializer.Meta):
        model = BulkProduct

class PremiumProductSerializer(ProductSerializer):
    class Meta(ProductSerializer.Meta):
        model = PremiumProduct