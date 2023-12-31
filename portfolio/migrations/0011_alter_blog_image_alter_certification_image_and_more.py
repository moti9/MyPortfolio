# Generated by Django 4.2.4 on 2023-09-02 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0010_familiartech_libframework_toolplatform_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="image",
            field=models.FileField(default=None, upload_to="blog/"),
        ),
        migrations.AlterField(
            model_name="certification",
            name="image",
            field=models.FileField(default=None, upload_to="certificate/"),
        ),
        migrations.AlterField(
            model_name="education",
            name="image",
            field=models.FileField(default=None, upload_to="education/"),
        ),
        migrations.AlterField(
            model_name="familiartech",
            name="image",
            field=models.FileField(default=None, upload_to="familiar/"),
        ),
        migrations.AlterField(
            model_name="interest",
            name="image",
            field=models.FileField(default=None, upload_to="interest/"),
        ),
        migrations.AlterField(
            model_name="language",
            name="image",
            field=models.FileField(default=None, upload_to="languages/"),
        ),
        migrations.AlterField(
            model_name="libframework",
            name="image",
            field=models.FileField(default=None, upload_to="frameworks/"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="profile_picture",
            field=models.FileField(
                blank=True, null=True, upload_to="profile_pictures/"
            ),
        ),
        migrations.AlterField(
            model_name="projectimage",
            name="image",
            field=models.FileField(default=None, upload_to="projects/"),
        ),
        migrations.AlterField(
            model_name="skill",
            name="image",
            field=models.FileField(default=None, upload_to="skill/"),
        ),
        migrations.AlterField(
            model_name="socialmedia",
            name="image",
            field=models.FileField(default=None, upload_to="social/"),
        ),
        migrations.AlterField(
            model_name="toolplatform",
            name="image",
            field=models.FileField(default=None, upload_to="tools/"),
        ),
        migrations.AlterField(
            model_name="workexperience",
            name="image",
            field=models.FileField(default=None, upload_to="work/"),
        ),
    ]
