# Generated by Django 4.0.3 on 2022-04-11 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_merge_20220411_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
    ]
