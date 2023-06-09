# Generated by Django 4.1.7 on 2023-02-23 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=False)),
                ('is_verify', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Societymember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('contact_no', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=20)),
                ('block_no', models.CharField(max_length=10)),
                ('occupation', models.CharField(max_length=10)),
                ('ownership', models.CharField(max_length=10)),
                ('dob', models.DateField(max_length=20)),
                ('no_of_familymembers', models.CharField(max_length=2)),
                ('blood_group', models.CharField(max_length=3)),
                ('vehicles_detils', models.CharField(max_length=20)),
                ('pic', models.FileField(default='media/s_default.png', upload_to='media/upload/societymember')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Chairman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('contact_no', models.CharField(max_length=30)),
                ('pic', models.FileField(default='media/c_deafault.png', upload_to='media/upload/chairman')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.user')),
            ],
        ),
    ]
