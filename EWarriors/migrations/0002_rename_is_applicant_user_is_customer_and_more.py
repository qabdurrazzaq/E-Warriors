# Generated by Django 4.0.3 on 2022-04-03 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EWarriors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_applicant',
            new_name='is_customer',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_company',
            new_name='is_dealer',
        ),
    ]
