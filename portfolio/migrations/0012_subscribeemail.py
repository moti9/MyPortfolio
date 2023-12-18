# Generated by Django 4.2.4 on 2023-09-02 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0011_alter_blog_image_alter_certification_image_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="SubscribeEmail",
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
                ("email", models.EmailField(max_length=100)),
                ("stamp", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]