# Generated by Django 3.2.10 on 2022-01-05 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='time_is_on',
            field=models.BooleanField(default=False),
        ),
    ]