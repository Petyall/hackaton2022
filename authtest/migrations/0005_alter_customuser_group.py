# Generated by Django 4.1.2 on 2022-10-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authtest', '0004_alter_customuser_group_alter_customuser_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='group',
            field=models.CharField(choices=[('', ''), ('ВИБ12', 'ВИБ12'), ('ВИБ22', 'ВИБ22'), ('ВИБ32', 'ВИБ32'), ('ВИБ42', 'ВИБ42')], default=' ', max_length=5, verbose_name='Группа'),
        ),
    ]