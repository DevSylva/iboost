# Generated by Django 4.1.5 on 2023-01-23 00:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0018_remove_transaction_charge_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="depositlog",
            name="time",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="time",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
