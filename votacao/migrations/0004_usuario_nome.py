# Generated by Django 5.1 on 2024-08-26 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votacao', '0003_remove_usuario_nome_usuario_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='nome',
            field=models.CharField(default=8, max_length=255),
            preserve_default=False,
        ),
    ]
