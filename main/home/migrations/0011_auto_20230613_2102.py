# Generated by Django 3.2.19 on 2023-06-13 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='featured_product',
            name='pro_slug',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='leatest_product',
            name='pro_slug',
            field=models.SlugField(null=True),
        ),
    ]
