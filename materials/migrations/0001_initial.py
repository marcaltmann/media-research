# Generated by Django 5.0.6 on 2024-06-24 18:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("archive", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transcript",
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
                (
                    "json",
                    models.JSONField(
                        default=list,
                        help_text="Paste the full transcript in JSON format.",
                        verbose_name="JSON file",
                    ),
                ),
                (
                    "vtt",
                    models.TextField(
                        default="",
                        help_text="Paste the full transcript in VTT format.",
                        verbose_name="VTT file",
                    ),
                ),
                ("language", models.CharField(max_length=5, verbose_name="language")),
                (
                    "resource",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="archive.resource",
                        verbose_name="resource",
                    ),
                ),
            ],
            options={
                "verbose_name": "transcript",
                "verbose_name_plural": "transcripts",
            },
        ),
    ]