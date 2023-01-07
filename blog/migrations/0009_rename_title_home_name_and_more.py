# Generated by Django 4.1.3 on 2022-11-23 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_home_delete_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='extendedinfo',
            new_name='profession',
        ),
        migrations.AlterField(
            model_name='home',
            name='description',
            field=models.TextField(default=False),
        ),
    ]