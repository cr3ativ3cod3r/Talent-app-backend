# Generated by Django 5.0.1 on 2024-02-09 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_item_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=100, null=True)),
                ('password', models.TextField(max_length=100, null=True)),
            ],
        ),
    ]
