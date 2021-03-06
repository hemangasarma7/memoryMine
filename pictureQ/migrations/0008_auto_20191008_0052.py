# Generated by Django 2.2.1 on 2019-10-07 19:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pictureQ', '0007_auto_20191008_0001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='photos',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='file_type',
        ),
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='album',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 10, 7, 19, 21, 59, 897840, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_date',
            field=models.DateField(default=datetime.datetime(2019, 10, 7, 19, 21, 59, 900340, tzinfo=utc)),
        ),
    ]
