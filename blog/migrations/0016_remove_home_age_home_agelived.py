# Generated by Django 4.1.3 on 2022-12-03 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_home_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='age',
        ),
        migrations.AddField(
            model_name='home',
            name='agelived',
            field=models.IntegerField(default=1),
        ),
    ]