# Generated by Django 4.0.4 on 2022-05-13 23:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("brands", "0002_alter_brand_name_alter_brand_slug"),
        ("products", "0005_product_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="brand",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="brands.brand",
            ),
        ),
    ]