# Generated by Django 4.1.5 on 2023-01-18 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0005_alter_user_address_alter_user_mobile_number_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="zipzcode",
            new_name="zipcode",
        ),
    ]
