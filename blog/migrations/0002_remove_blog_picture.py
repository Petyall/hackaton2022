# Generated by Django 4.1.2 on 2022-10-22 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='picture',
        ),
    ]
