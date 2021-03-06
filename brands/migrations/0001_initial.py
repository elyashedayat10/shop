# Generated by Django 4.0.4 on 2022-05-13 22:55

from django.db import migrations, models

import helpers


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Brand",
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
                ("name", models.CharField(max_length=125, unique=True)),
                ("slug", models.SlugField()),
                ("image", models.ImageField(upload_to=helpers.get_file_path)),
            ],
        ),
    ]
