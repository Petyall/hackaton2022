# Generated by Django 4.1.2 on 2022-10-22 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authtest', '0005_alter_customuser_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='type',
            field=models.CharField(choices=[('', ''), ('Преподаватель', 'Преподаватель'), ('Сотрудник', 'Сотрудник')], default=' ', max_length=20, verbose_name='Тип'),
        ),
    ]
