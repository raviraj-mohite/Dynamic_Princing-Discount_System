from rest_framework import viewsets

from system.models import Discount
from system.serializers.discount_serializer import DiscountSerializer


class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer