# Generated by Django 5.0.6 on 2024-06-26 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("entities", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="entity",
            name="description",
            field=models.TextField(blank=True, verbose_name="description"),
        ),
        migrations.AddField(
            model_name="person",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True, verbose_name="date of birth"),
        ),
        migrations.AddField(
            model_name="person",
            name="date_of_death",
            field=models.DateField(blank=True, null=True, verbose_name="date of death"),
        ),
    ]
