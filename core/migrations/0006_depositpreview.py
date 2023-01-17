# Generated by Django 4.1.5 on 2023-01-17 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_alter_instagramservice_service_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="DepositPreview",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.FloatField(default=0)),
            ],
        ),
    ]