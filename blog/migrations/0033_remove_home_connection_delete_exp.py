# Generated by Django 4.1.3 on 2022-12-10 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_alter_home_connection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='connection',
        ),
        migrations.DeleteModel(
            name='Exp',
        ),
    ]
