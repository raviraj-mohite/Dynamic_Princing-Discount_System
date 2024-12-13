from rest_framework import serializers

from system.models import Order, Product, Discount
from system.serializers.discount_serializer import DiscountSerializer
from system.serializers.product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    discounts = DiscountSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'products', 'discounts']

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        discounts_data = validated_data.pop('discounts')
        order = Order.objects.create(**validated_data)
        for product_data in products_data:
            product = Product.objects.get(id=product_data['id'])
            order.products.add(product)
        for discount_data in discounts_data:
            discount = Discount.objects.get(id=discount_data['id'])
            order.discounts.add(discount)
        return order