# Generated by Django 2.2.1 on 2019-10-19 22:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictureQ', '0012_auto_20191008_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 10, 20, 3, 45, 54, 940923)),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_date',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 10, 20, 3, 45, 54, 941924), null=True),
        ),
    ]
