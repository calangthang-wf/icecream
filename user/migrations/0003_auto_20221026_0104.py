# Generated by Django 3.2.16 on 2022-10-25 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20221026_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_user',
            name='fist_name',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='register_user',
            name='last_name',
            field=models.TextField(max_length=10),
        ),
    ]