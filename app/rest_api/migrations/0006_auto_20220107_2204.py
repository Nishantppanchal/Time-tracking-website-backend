# Generated by Django 3.2.10 on 2022-01-07 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0005_auto_20220107_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timers',
            name='end_time',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='timers',
            name='start_time',
            field=models.IntegerField(),
        ),
    ]
