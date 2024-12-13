from django.db import models


class Discount(models.Model):
    name = models.CharField(max_length=100)
    priority = models.IntegerField()

    def apply_discount(self, price):
        pass

class PercentageDiscount(Discount):
    percentage = models.FloatField()

    def apply_discount(self, price):
        return price * (1 - self.percentage / 100)

class FixedAmountDiscount(Discount):
    amount = models.FloatField()

    def apply_discount(self, price):
        return price - self.amount

class TieredDiscount(Discount):
    tier_1_threshold = models.FloatField(default=500)
    tier_2_threshold = models.FloatField(default=1000)
    tier_1_discount = models.FloatField(default=0.05)  # 5% off for $500-$1000
    tier_2_discount = models.FloatField(default=0.10)  # 10% off for >$1000

    def apply_discount(self, price):
        if price < self.tier_1_threshold:
            return price
        elif price <= self.tier_2_threshold:
            return price * (1 - self.tier_1_discount)
        else:
            return price * (1 - self.tier_2_discount)