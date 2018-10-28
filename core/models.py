from django.db import models

# Create your models here.

class Vivienda(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class Region(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Region"
        verbose_name_plural= "Regiones"

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural= "Ciudades"

class Postulante(models.Model):
    nombre = models.CharField(max_length=300)
    run = models.CharField(max_length=12, unique=True)
    fechaNacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE)
    telefono = models.IntegerField()
    correo = models.EmailField()

    def __str__(self):
        return self.run

class Raza(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    

class Estado(models.Model):
    descripcion = models.CharField(max_length = 50)

    def __str__(self):
        return self.descripcion

class Mascota(models.Model):
    nombre = models.CharField(max_length = 100)
    raza =  models.ForeignKey(Raza, on_delete = models.CASCADE)
    genero = models.CharField(max_length = 50)
    fechaIngreso = models.DateField()
    fechaNacimiento = models.DateField()
    descripcion = models.CharField(max_length = 500)
    estado = models.ForeignKey(Estado, on_delete = models.CASCADE)
    imagen_mascota = models.FileField(blank=True)

    def __str__(self):
        return self.nombre