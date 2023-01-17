# Generated by Django 4.1.5 on 2023-01-17 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_youtubeservice"),
    ]

    operations = [
        migrations.AlterField(
            model_name="instagramservice",
            name="service",
            field=models.CharField(
                choices=[
                    (
                        "Real Nigerian Instagram Follower",
                        "Real Nigerian Instagram Follower",
                    ),
                    (
                        "Instagram Reach + Impressions + Profile Visits [Post Link]",
                        "Instagram Reach + Impressions + Profile Visits [Post Link]",
                    ),
                    (
                        "Instagram Reach + Impressions [Post Link]",
                        "Instagram Reach + Impressions [Post Link]",
                    ),
                    ("Instagram Emoji Comments", "Instagram Emoji Comments"),
                    ("Instagram Random Comments", "Instagram Random Comments"),
                    ("Instagram Likes [Post Link]", "Instagram Likes [Post Link]"),
                    ("Instagram Followers", "Instagram Followers"),
                ],
                default=(
                    "Real Nigerian Instagram Follower",
                    "Real Nigerian Instagram Follower",
                ),
                max_length=200,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="tiktokservice",
            name="service",
            field=models.CharField(
                choices=[
                    ("Tiktok Like [Post Link]", "Tiktok Like [Post Link]"),
                    ("TikTok Followers", "TikTok Followers"),
                    (
                        "Cheapest TikTok Video Views [Post Link]",
                        "Cheapest TikTok Video Views [Post Link]s",
                    ),
                ],
                default=("Tiktok Like [Post Link]", "Tiktok Like [Post Link]"),
                max_length=200,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="youtubeservice",
            name="service",
            field=models.CharField(
                choices=[
                    ("Youtube Views [RECOMMENDED]", "Youtube Views [RECOMMENDED]"),
                    ("Youtube Subscribers", "Youtube Subscribers"),
                    ("Youtube Likes", "Youtube Likes"),
                ],
                default=("Youtube Views [RECOMMENDED]", "Youtube Views [RECOMMENDED]"),
                max_length=200,
                unique=True,
            ),
        ),
    ]