# Generated by Django 5.0.9 on 2024-11-26 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0003_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
