# Generated by Django 4.1.3 on 2022-12-13 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='experience',
            field=models.CharField(default='Fock', max_length=100),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='salary',
            field=models.CharField(default='Fock', max_length=100),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='schedule',
            field=models.CharField(default='Fock', max_length=100),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='name',
            field=models.CharField(default='Fock', max_length=100),
        ),
    ]