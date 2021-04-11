# Generated by Django 3.1.7 on 2021-04-02 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('villapp', '0012_auto_20210402_0623'),
    ]

    operations = [
        migrations.CreateModel(
            name='TasadelMes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tabla', models.CharField(max_length=10)),
                ('Tenero', models.IntegerField(null=True)),
                ('DolarenEnero', models.IntegerField(null=True)),
                ('Tfebrero', models.IntegerField(null=True)),
                ('Dolarenfebrero', models.IntegerField(null=True)),
                ('Tmarzo', models.IntegerField(null=True)),
                ('Dolarenmarzo', models.IntegerField(null=True)),
                ('Tabril', models.IntegerField(null=True)),
                ('Dolarenabril', models.IntegerField(null=True)),
                ('Tmayo', models.IntegerField(null=True)),
                ('Dolarenmayo', models.IntegerField(null=True)),
                ('Tjunio', models.IntegerField(null=True)),
                ('Dolarenjunio', models.IntegerField(null=True)),
                ('Tjulio', models.IntegerField(null=True)),
                ('Dolarenjulio', models.IntegerField(null=True)),
                ('Tagosto', models.IntegerField(null=True)),
                ('Dolarenagosto', models.IntegerField(null=True)),
                ('Tseptiembre', models.IntegerField(null=True)),
                ('Dolarenseptiembre', models.IntegerField(null=True)),
                ('Toctubre', models.IntegerField(null=True)),
                ('Dolarenoctubre', models.IntegerField(null=True)),
                ('Tnoviembre', models.IntegerField(null=True)),
                ('Dolarennoviembre', models.IntegerField(null=True)),
                ('Tdiciembre', models.IntegerField(null=True)),
                ('Dolarendicimebre', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.AddField(
            model_name='profile',
            name='Monto',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='apellido',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='casaN',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='cedula',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='nombre',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.CreateModel(
            name='Deudas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deuda', models.IntegerField(max_length=300)),
                ('Enero', models.BooleanField(default=False, verbose_name=': Enero')),
                ('Febrero', models.BooleanField(default=False, verbose_name=': Febrero')),
                ('Marzo', models.BooleanField(default=False, verbose_name=': Marzo')),
                ('Abril', models.BooleanField(default=False, verbose_name=': Abril')),
                ('Mayo', models.BooleanField(default=False, verbose_name=': Mayo')),
                ('Junio', models.BooleanField(default=False, verbose_name=': Junio')),
                ('Julio', models.BooleanField(default=False, verbose_name=': Julio')),
                ('Agosto', models.BooleanField(default=False, verbose_name=': Agosto')),
                ('Septiembre', models.BooleanField(default=False, verbose_name=': Septiembre')),
                ('Octubre', models.BooleanField(default=False, verbose_name=': Octubre')),
                ('Noviembre', models.BooleanField(default=False, verbose_name=': Noviembre')),
                ('Diciembre', models.BooleanField(default=False, verbose_name=': Diciembre')),
                ('Tabla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='villapp.tasadelmes')),
                ('nombreD', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='villapp.profile')),
            ],
        ),
    ]