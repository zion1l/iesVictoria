from django.db import models
from django.utils import timezone


class Perfiles(models.Model):
    id = models.AutoField(primary_key=True)
    perfil= models.CharField(max_length=50)

class Usuarios_Perfiles(models.Model):
    id_usuario = models.ForeignKey("auth.user", on_delete=None, null=False, blank=False)
    id_perfil = models.ForeignKey("Perfiles", on_delete=None, null=False, blank=False)

class Asignaturas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

#class Notas(models.Model):
 #   modulo = models.ChoiceeField(choices=(('deberes','Deberes'),('trabajos','Trabajos'),('examenes','Exámenes')))
  #  fecha = models.DateField()
   # comentario = models.CharField(max_length=200)
    #nota = models.FloatField()
    #trimestre = models.ChoiceField(choices=(('1','Primero'),('2','Segundo'),('3','Tercero')))