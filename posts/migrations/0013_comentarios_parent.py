# Generated by Django 4.0 on 2022-08-28 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_alter_comentarios_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentarios',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='posts.comentarios'),
        ),
    ]
