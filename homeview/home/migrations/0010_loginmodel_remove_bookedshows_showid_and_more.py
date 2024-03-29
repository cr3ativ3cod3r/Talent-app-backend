# Generated by Django 5.0.1 on 2024-02-11 07:04

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_rename_register_registermodel'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Loginmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=100, null=True)),
                ('password', models.TextField(max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='bookedshows',
            name='showID',
        ),
        migrations.AddField(
            model_name='bookedshows',
            name='id_key',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='item',
            name='time',
            field=models.TimeField(null=True, verbose_name=datetime.datetime(2024, 2, 11, 7, 4, 59, 485903)),
        ),
    ]
