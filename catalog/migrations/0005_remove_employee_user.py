# Generated by Django 2.2 on 2020-10-24 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20201025_0010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
    ]