# Generated by Django 4.1.3 on 2022-12-14 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainInfo', '0004_stats'),
    ]

    operations = [
        migrations.AddField(
            model_name='stats',
            name='name',
            field=models.CharField(default='stats', max_length=100),
        ),
    ]
