# Generated by Django 2.1.5 on 2019-03-28 21:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('philm', '0004_auto_20190328_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='reviews_updated',
        ),
        migrations.AlterField(
            model_name='reviews',
            name='reviews_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
