# Generated by Django 4.1.7 on 2023-02-23 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chairmanapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chairman',
            name='pic',
            field=models.FileField(default='media/c_default.png', upload_to='media/upload/chairman'),
        ),
    ]