# Generated by Django 5.1.4 on 2024-12-13 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_fixedamountdiscount_percentagediscount_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductDiscount',
        ),
    ]
