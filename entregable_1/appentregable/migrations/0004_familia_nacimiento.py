# Generated by Django 4.1 on 2022-08-27 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appentregable', '0003_remove_familia_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='familia',
            name='nacimiento',
            field=models.DateField(null=True),
        ),
    ]
