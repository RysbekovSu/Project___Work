# Generated by Django 4.1.3 on 2022-12-06 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_info_connection'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='connection',
            field=models.ManyToManyField(blank=True, related_name='include', to='blog.exp'),
        ),
        migrations.DeleteModel(
            name='INFO',
        ),
    ]
