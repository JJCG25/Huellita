from django.db import models

#Clase para el perrito

class Perrito(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    raza = models.CharField(max_length=100)
    descripcion = models.TextField()
    tamano = models.CharField(max_length=50, choices=[('Pequeño', 'Pequeño'), ('Mediano', 'Mediano'), ('Grande', 'Grande')])
    foto = models.ImageField(upload_to='fotos_perritos/')
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
#Clase para la Veterinaria

class Veterinaria(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    servicios = models.TextField()
    horario_atencion = models.CharField(max_length=100)
    ubicacion_mapa = models.URLField(blank=True)  # URL para integración con Google Maps

    def __str__(self):
        return self.nombre
    
#Clase para el Cuidador

class Cuidador(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    experiencia = models.TextField()
    servicios = models.TextField()
    tarifas = models.CharField(max_length=100, blank=True)
    foto_perfil = models.ImageField(upload_to='cuidadores/', blank=True)

    def __str__(self):
        return self.nombre
