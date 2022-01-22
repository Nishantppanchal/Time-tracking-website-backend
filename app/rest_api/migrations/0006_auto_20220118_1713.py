# Generated by Django 3.2.10 on 2022-01-18 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0005_alter_tags_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='tags',
            field=models.ManyToManyField(blank=True, to='rest_api.tags'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
