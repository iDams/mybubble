# Generated by Django 2.2.4 on 2019-10-01 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0006_auto_20191001_1944'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Preguntas',
            new_name='Pregunta',
        ),
        migrations.RenameModel(
            old_name='Respuesta',
            new_name='Respuestas',
        ),
    ]