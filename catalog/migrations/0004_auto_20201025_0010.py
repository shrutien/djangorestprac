# Generated by Django 2.2 on 2020-10-24 18:40

import catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20201024_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(max_length=200, unique=True, validators=[catalog.models.phone_validation]),
        ),
    ]