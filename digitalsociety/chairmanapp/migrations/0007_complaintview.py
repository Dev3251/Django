# Generated by Django 4.1.7 on 2023-03-04 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chairmanapp', '0006_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplaintView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('complaint_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.complaint')),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.societymember')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.user')),
            ],
        ),
    ]
