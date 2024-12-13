from rest_framework import serializers

from system.models import Discount


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['id', 'name', 'priority', 'percentage', 'amount', 'tier_1_threshold', 'tier_2_threshold', 'tier_1_discount', 'tier_2_discount']
