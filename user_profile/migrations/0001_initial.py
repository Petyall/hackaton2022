# Generated by Django 4.1.2 on 2022-10-21 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(blank=True, max_length=50, null=True)),
                ('comment', models.FileField(upload_to='schedule/')),
            ],
            options={
                'verbose_name': 'Расписания',
                'verbose_name_plural': 'Расписания',
                'ordering': ['pk'],
            },
        ),
    ]