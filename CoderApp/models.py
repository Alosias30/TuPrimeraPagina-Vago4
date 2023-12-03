from django.db import models

# Create your models here.

class Comentario(models.Model):
    nombre = models.CharField(max_length=50)
    comentario = models.CharField(max_length=300)

class Destino(models.Model):
    nombre = models.CharField(max_length=50)
    comentario = models.CharField(max_length=300)

class Restaurant(models.Model):
    nombre = models.CharField(max_length=50)
    comentario = models.CharField(max_length=300)