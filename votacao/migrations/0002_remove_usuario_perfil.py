# Generated by Django 5.1 on 2024-08-26 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votacao', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='perfil',
        ),
    ]
