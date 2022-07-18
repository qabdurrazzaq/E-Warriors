# Generated by Django 4.0.3 on 2022-04-11 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0008_merge_20220411_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellwaste',
            name='pickup_point',
        ),
        migrations.AlterField(
            model_name='sellwaste',
            name='active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='sellwaste',
            name='is_admins',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='sellwaste',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True),
        ),
    ]
