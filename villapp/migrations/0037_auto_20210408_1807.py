# Generated by Django 3.1.7 on 2021-04-08 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('villapp', '0036_deudas_deudadepago'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relationship',
            name='from_user',
        ),
        migrations.RemoveField(
            model_name='relationship',
            name='to_user',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Relationship',
        ),
    ]
