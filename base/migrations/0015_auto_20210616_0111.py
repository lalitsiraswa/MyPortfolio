# Generated by Django 3.2.4 on 2021-06-15 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_skill_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
