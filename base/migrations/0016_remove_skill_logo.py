# Generated by Django 3.2.4 on 2021-06-15 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_auto_20210616_0111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='logo',
        ),
    ]