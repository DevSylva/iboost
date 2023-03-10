# Generated by Django 4.1.5 on 2023-01-21 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0015_orderhistory"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="orderhistory",
            options={
                "verbose_name": "Order History",
                "verbose_name_plural": "Order Histories",
            },
        ),
        migrations.AddField(
            model_name="depositlog",
            name="amount",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
