# Generated by Django 4.1.5 on 2023-01-19 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_alter_service_service"),
    ]

    operations = [
        migrations.AddField(
            model_name="depositpreview",
            name="method",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]