# Generated by Django 3.2.4 on 2021-06-16 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(choices=[('fullstack', 'fullstack'), ('frontend', 'frontend'), ('backend', 'backend')], max_length=200),
        ),
    ]
