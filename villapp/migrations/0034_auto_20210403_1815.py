# Generated by Django 3.1.7 on 2021-04-03 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('villapp', '0033_remove_deudas_deudatotal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deudas',
            name='PagodeAbril',
        ),
        migrations.RemoveField(
            model_name='deudas',
            name='PagodeAgosto',
        ),
        migrations.RemoveField(
            model_name='deudas',
            name='PagodeDiciembre',
        ),
        migrations.RemoveField(
            model_name='deudas',
            name='PagodeEnero',
        ),
        migrations.RemoveField(
            model_name='deudas',
            name='PagodeFebrero',
        ),
        migrations.RemoveField(
            model_name='deudas',
            name='PagodeJulio',
        ),
        migrations.RemoveField(
            model_name='deudas',
            name='PagodeJunio',
        ),
        migrations.RemoveField(
            model_name='deudas',
            name='PagodeMarzo',
        ),
        migrations.RemoveField(
            model_name='deudas',
            name='PagodeMayo',
        ),
        migrations.RemoveField(
            model_name='deudas',
            name='PagodeNoviembre',
        ),
        migrations.RemoveField(
            model_name='deudas',
            name='PagodeOctubre',
        ),
        migrations.RemoveField(
            model_name='deudas',
            name='PagodeSeptiembre',
        ),
    ]