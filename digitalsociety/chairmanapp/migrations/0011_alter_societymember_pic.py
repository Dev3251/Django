# Generated by Django 4.1.7 on 2023-03-24 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chairmanapp', '0010_user_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='societymember',
            name='pic',
            field=models.FileField(default='media/s_default.png', null=True, upload_to='media/upload/societymember'),
        ),
    ]
