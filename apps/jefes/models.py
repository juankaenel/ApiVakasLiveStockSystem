from django.db import models
from apps.users.models import Usuario


class Jefes(models.Model):
    """
    Modelo Jefes
    """
    cuig = models.CharField(max_length=45)
    renspa = models.CharField(max_length=45)
    sena = models.CharField(max_length=45)
    marca = models.CharField(max_length=45)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE) #relación muchos a uno con Usuario

    # def __str__(self):
    #     return self.user
