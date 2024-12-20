# Generated by Django 5.1.3 on 2024-11-25 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuidador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=254)),
                ('experiencia', models.TextField()),
                ('servicios', models.TextField()),
                ('tarifas', models.CharField(blank=True, max_length=100)),
                ('foto_perfil', models.ImageField(blank=True, upload_to='cuidadores/')),
            ],
        ),
        migrations.CreateModel(
            name='Perrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('edad', models.PositiveIntegerField()),
                ('raza', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('tamano', models.CharField(choices=[('Pequeño', 'Pequeño'), ('Mediano', 'Mediano'), ('Grande', 'Grande')], max_length=50)),
                ('foto', models.ImageField(upload_to='fotos_perritos/')),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Veterinaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=254)),
                ('servicios', models.TextField()),
                ('horario_atencion', models.CharField(max_length=100)),
                ('ubicacion_mapa', models.URLField(blank=True)),
            ],
        ),
    ]
