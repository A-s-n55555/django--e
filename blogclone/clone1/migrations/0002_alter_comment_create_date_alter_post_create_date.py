# Generated by Django 4.1.5 on 2023-01-18 15:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clone1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 18, 15, 43, 53, 448055, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 18, 15, 43, 53, 448055, tzinfo=datetime.timezone.utc)),
        ),
    ]