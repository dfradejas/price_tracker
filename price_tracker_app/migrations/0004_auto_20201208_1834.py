# Generated by Django 2.2.12 on 2020-12-08 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_tracker_app', '0003_auto_20201208_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(),
        ),
    ]