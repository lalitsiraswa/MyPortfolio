# Generated by Django 3.2.4 on 2021-06-15 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_skill_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
