# Generated by Django 3.2.4 on 2021-06-27 11:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210627_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 27, 11, 24, 39, 216835), verbose_name='date published'),
        ),
    ]
