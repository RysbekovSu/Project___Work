# Generated by Django 4.1.3 on 2022-12-18 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainInfo', '0007_popularteachers_instagram_popularteachers_telegram_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutInai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='Inai twe')),
                ('image', models.ImageField(default='i', upload_to='')),
            ],
        ),
    ]