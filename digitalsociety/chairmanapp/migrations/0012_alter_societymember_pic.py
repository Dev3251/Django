# Generated by Django 4.1.7 on 2023-03-24 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chairmanapp', '0011_alter_societymember_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='societymember',
            name='pic',
            field=models.FileField(default='media/s_default.png', upload_to='media/upload/societymember'),
        ),
    ]