# Generated by Django 2.2.2 on 2019-10-01 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('rut', models.CharField(max_length=12, primary_key=True, serialize=False)),
            ],
        ),
    ]