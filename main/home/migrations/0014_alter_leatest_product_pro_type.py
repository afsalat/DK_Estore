# Generated by Django 3.2.19 on 2023-08-04 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20230623_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leatest_product',
            name='pro_type',
            field=models.CharField(choices=[('lt', 'leatest')], default=(('lt', 'leatest'),), max_length=50, null=True),
        ),
    ]