# Generated by Django 3.2.10 on 2022-01-18 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0003_alter_logs_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
    ]
