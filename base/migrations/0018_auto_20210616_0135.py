# Generated by Django 3.2.4 on 2021-06-15 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_skill_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='logo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
