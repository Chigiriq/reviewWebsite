# Generated by Django 5.0.9 on 2024-12-05 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0005_merge_0002_product_image_0004_alter_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
