# Generated by Django 4.1.5 on 2023-01-17 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0003_user_address_user_city_user_profile_pic_user_state_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="zipzcoe",
            new_name="zipzcode",
        ),
    ]
