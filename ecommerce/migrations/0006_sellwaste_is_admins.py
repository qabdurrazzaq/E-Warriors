# Generated by Django 4.0.3 on 2022-04-11 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_alter_sellwaste_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellwaste',
            name='is_admins',
            field=models.BooleanField(default=False),
        ),
    ]
