# Generated by Django 3.2.4 on 2021-06-27 10:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_tutorial_tutorial_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 27, 10, 57, 23, 891190), verbose_name='date published'),
        ),
    ]
