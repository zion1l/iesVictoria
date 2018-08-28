from django.db import models
from django.utils import timezone



class Perfiles(models.Model):
    id = models.AutoField(primary_key=True)
    perfil= models.CharField(max_length=50)

class Usuarios_Perfiles(models.Model):
    id_usuario = models.ForeignKey("auth.user", on_delete=None, null=False, blank=False)
    id_perfil = models.ForeignKey("Perfiles", on_delete=None, null=False, blank=False)