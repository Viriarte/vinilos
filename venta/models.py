from django.db import models

# Create your models here.

    
    
class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True) 
    genero = models.CharField(max_length=40, blank=False, null=False)

    def __str__(self):
        return self.genero


class Album(models.Model):
    id_album           = models.CharField(primary_key=True, max_length=10)
    titulo             = models.CharField(max_length=20)
    id_genero         = models.ForeignKey('Genero', on_delete=models.CASCADE, db_column='idGenero', related_name='albums')
    lanzamiento        = models.DateField(blank=False, null=False) 
    genero             = models.CharField(max_length=20)
    cantidad_canciones = models.CharField(max_length=20)
    tracklist          = models.TextField(blank=True, null=True)
    duracion           = models.CharField(max_length=45)
    notas              = models.CharField(max_length=3)
    disponibilidad     = models.IntegerField()

    def __str__(self):
        return self.titulo
