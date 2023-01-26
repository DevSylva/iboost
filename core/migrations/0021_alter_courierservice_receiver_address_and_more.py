# Generated by Django 4.1.5 on 2023-01-25 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0020_courierservice"),
    ]

    operations = [
        migrations.AlterField(
            model_name="courierservice",
            name="receiver_address",
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name="courierservice",
            name="receiver_email",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="courierservice",
            name="sender_address",
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name="courierservice",
            name="sender_email",
            field=models.CharField(max_length=150),
        ),
    ]
