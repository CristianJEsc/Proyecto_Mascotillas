
from django.db import models

class Mascotas(models.Model):
    animal=models.CharField(max_length=40)
    raza=models.CharField(max_length=40)
    nombre=models.CharField(max_length=40)
    fecha_nacimiento=models.DateField()
   

class Productos(models.Model):
    nombre=models.CharField(max_length=40)
    marca=models.CharField(max_length=40)
    precio= models.IntegerField()
    

class Servicios(models.Model):
    nombre=models.CharField(max_length=40)
    precio= models.IntegerField()


