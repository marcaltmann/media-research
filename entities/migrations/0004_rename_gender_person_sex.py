# Generated by Django 5.0.6 on 2024-06-26 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("entities", "0003_person_gender"),
    ]

    operations = [
        migrations.RenameField(
            model_name="person",
            old_name="gender",
            new_name="sex",
        ),
    ]