# Generated by Django 4.1 on 2022-08-27 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appentregable', '0006_familia_nacimiento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familia',
            name='nacimiento',
        ),
    ]
