# Generated by Django 4.2.4 on 2023-09-01 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0008_interest_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactMessage",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=200)),
                ("message", models.TextField()),
                ("reviewed", models.BooleanField(default=False)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
