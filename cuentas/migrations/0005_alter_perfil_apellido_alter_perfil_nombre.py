# Generated by Django 4.0 on 2022-08-28 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0004_perfil_apellido_perfil_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='apellido',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre'),
        ),
    ]
