# Generated by Django 4.1.2 on 2022-10-22 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authtest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='group',
            field=models.CharField(choices=[('vib12', 'ВИБ12'), ('vib22', 'ВИБ22')], default='', max_length=5, verbose_name='Пол'),
        ),
    ]
