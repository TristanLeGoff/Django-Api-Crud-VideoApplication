# Generated by Django 3.1.3 on 2020-11-11 11:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='date_field',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 11, 12, 8, 16, 246070)),
        ),
    ]
