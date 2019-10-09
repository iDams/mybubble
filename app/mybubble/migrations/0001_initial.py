# Generated by Django 2.2.4 on 2019-10-03 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('idAvatar', models.AutoField(primary_key=True, serialize=False)),
                ('imagen', models.CharField(max_length=50)),
                ('puntosAvatar', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('idCurso', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCurso', models.CharField(max_length=30)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id_Pregunta', models.AutoField(primary_key=True, serialize=False)),
                ('pregunta', models.CharField(max_length=100)),
                ('activopregunta', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Usuario',
            fields=[
                ('idTipoUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('run', models.CharField(max_length=12)),
                ('nombre', models.CharField(max_length=25)),
                ('apaterno', models.CharField(max_length=25)),
                ('apmaterno', models.CharField(max_length=25)),
                ('correo', models.EmailField(max_length=50)),
                ('activo', models.BooleanField(default=True)),
                ('puntos', models.IntegerField(default=0)),
                ('idAvatar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mybubble.Avatar')),
                ('idCurso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mybubble.Curso')),
                ('idTipoUsuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mybubble.Tipo_Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id_Respuesta', models.AutoField(primary_key=True, serialize=False)),
                ('respuestas', models.CharField(max_length=100)),
                ('correcta', models.BooleanField(default=False)),
                ('idUsuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mybubble.Usuario')),
                ('id_Pregunta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mybubble.Pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='Puente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idUsuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mybubble.Usuario')),
                ('id_Pregunta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mybubble.Pregunta')),
                ('id_Respuesta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mybubble.Respuesta')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('idComentario', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=250)),
                ('idUsuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mybubble.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('idAsignatura', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombreAsigantura', models.CharField(max_length=15)),
                ('activo', models.BooleanField(default=True)),
                ('idcurso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mybubble.Curso')),
            ],
        ),
    ]
