# Generated by Django 4.1.5 on 2023-01-25 00:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0019_alter_depositlog_time_alter_transaction_time"),
    ]

    operations = [
        migrations.CreateModel(
            name="CourierService",
            fields=[
                (
                    "tracking_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("sender_full_name", models.CharField(max_length=150)),
                ("sender_company_name", models.CharField(max_length=150)),
                ("sender_address", models.TextField(default="enter address")),
                ("sender_country", models.CharField(max_length=150)),
                ("sender_city", models.CharField(max_length=150)),
                ("sender_state_province", models.CharField(max_length=150)),
                ("sender_postal_code", models.CharField(max_length=150)),
                ("sender_phone_number", models.CharField(max_length=150)),
                ("sender_email", models.EmailField(max_length=254)),
                ("sender_type", models.CharField(max_length=150)),
                ("receiver_full_name", models.CharField(max_length=150)),
                ("receiver_company_name", models.CharField(max_length=150)),
                ("receiver_address", models.TextField(default="enter address")),
                ("receiver_country", models.CharField(max_length=150)),
                ("receiver_city", models.CharField(max_length=150)),
                ("receiver_state_province", models.CharField(max_length=150)),
                ("receiver_postal_code", models.CharField(max_length=150)),
                ("receiver_phone_number", models.CharField(max_length=150)),
                ("receiver_email", models.EmailField(max_length=254)),
            ],
        ),
    ]
