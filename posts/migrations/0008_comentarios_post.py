# Generated by Django 4.0 on 2022-08-26 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_comentarios_dislikes_comentarios_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentarios',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='posts.post'),
            preserve_default=False,
        ),
    ]