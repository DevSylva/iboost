# Generated by Django 4.1.5 on 2023-01-21 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_instagramservice_tiktokservice_youtubeservice_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="instagramservice",
            name="service_id",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="tiktokservice",
            name="service_id",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="youtubeservice",
            name="service_id",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
