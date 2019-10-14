# Generated by Django 2.2.4 on 2019-10-01 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_auto_20191001_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preguntas',
            fields=[
                ('id_Pregunta', models.AutoField(primary_key=True, serialize=False)),
                ('pregunta', models.CharField(max_length=100)),
                ('activopregunta', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='run',
            field=models.CharField(max_length=12),
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id_Respuesta', models.AutoField(primary_key=True, serialize=False)),
                ('respuestas', models.CharField(max_length=100)),
                ('correcta', models.BooleanField(default=False)),
                ('idUsuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuario.Usuario')),
                ('id_Pregunta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuario.Preguntas')),
            ],
        ),
        migrations.CreateModel(
            name='Puente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idUsuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuario.Usuario')),
                ('id_Pregunta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuario.Preguntas')),
                ('id_Respuesta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuario.Respuesta')),
            ],
        ),
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('idAsignatura', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombreAsigantura', models.CharField(max_length=15)),
                ('activo', models.BooleanField(default=True)),
                ('idcurso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuario.Curso')),
            ],
        ),
    ]