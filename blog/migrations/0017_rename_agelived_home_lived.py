# Generated by Django 4.1.3 on 2022-12-03 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_remove_home_age_home_agelived'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='agelived',
            new_name='lived',
        ),
    ]
