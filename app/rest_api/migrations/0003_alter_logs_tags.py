# Generated by Django 3.2.10 on 2022-01-18 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='rest_api.tags'),
        ),
    ]
