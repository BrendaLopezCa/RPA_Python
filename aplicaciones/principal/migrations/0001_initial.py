# Generated by Django 3.2.9 on 2021-11-12 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('matricula', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('facultad', models.CharField(max_length=50)),
                ('carrera', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=150)),
            ],
        ),
    ]
