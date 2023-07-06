from django.db import models

# Create your models here.

class Artista(models.Model):
    nombre = models.CharField(max_length=70)
    
    def __str__(self):
        return self.nombre

class Album(models.Model):
    titulo = models.CharField(max_length=70)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    genero = models.CharField(max_length=70)
    imagen = models.ImageField(upload_to = "albums", null=True)
    artista = models.ForeignKey(Artista, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.titulo
