# Generated by Django 4.0.4 on 2022-05-13 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("brands", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="brand",
            name="name",
            field=models.CharField(max_length=125),
        ),
        migrations.AlterField(
            model_name="brand",
            name="slug",
            field=models.SlugField(unique=True),
        ),
    ]
