# Generated by Django 4.0.4 on 2022-06-01 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='created',
        ),
    ]
