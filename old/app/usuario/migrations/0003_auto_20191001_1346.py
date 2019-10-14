# Generated by Django 2.2.2 on 2019-10-01 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20191001_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Usuario',
            fields=[
                ('idTipoUsuario', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=10)),
            ],
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='appaterno',
            new_name='apaterno',
        ),
        migrations.AddField(
            model_name='usuario',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='puntos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='idTipoUsuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuario.Tipo_Usuario'),
        ),
    ]