# Generated by Django 3.2.10 on 2022-01-18 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0004_alter_tags_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]