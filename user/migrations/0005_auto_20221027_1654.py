# Generated by Django 3.2.16 on 2022-10-27 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20221026_0330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='fist_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]
