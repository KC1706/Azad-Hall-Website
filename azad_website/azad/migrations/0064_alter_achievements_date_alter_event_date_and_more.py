# Generated by Django 4.1.4 on 2024-01-12 13:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azad', '0063_alter_achievements_date_alter_event_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievements',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 12, 13, 43, 2, 448274)),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 12, 13, 43, 2, 445575)),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 12, 13, 43, 2, 446746)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 12, 13, 43, 2, 447752)),
        ),
        migrations.AlterField(
            model_name='para',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 12, 13, 43, 2, 446048)),
        ),
    ]