# Generated by Django 2.2.12 on 2020-12-08 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_tracker_app', '0005_auto_20201208_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='price',
        ),
        migrations.AddField(
            model_name='item',
            name='initPrice',
            field=models.FloatField(default=0),
        ),
    ]
