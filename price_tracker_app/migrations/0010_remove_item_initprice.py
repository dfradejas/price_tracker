# Generated by Django 3.1.4 on 2020-12-08 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price_tracker_app', '0009_auto_20201208_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='initPrice',
        ),
    ]
