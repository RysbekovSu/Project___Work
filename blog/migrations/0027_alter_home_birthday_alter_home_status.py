# Generated by Django 4.1.3 on 2022-12-03 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_home_experience_home_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='birthday',
            field=models.CharField(default='xx.xx.xx', max_length=40),
        ),
        migrations.AlterField(
            model_name='home',
            name='status',
            field=models.CharField(max_length=20),
        ),
    ]
