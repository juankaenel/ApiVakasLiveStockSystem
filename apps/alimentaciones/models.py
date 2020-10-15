from django.db import models

from apps.alimentos.models import Alimentos


class Alimentaciones(models.Model):
    """
    Modelo alimentaciones
    """
    cantidad = models.IntegerField()
    descripcion = models.TextField(default='', blank=True)
    alimentos = models.ForeignKey(Alimentos, on_delete=models.CASCADE)
    #empleados = models.ForeignKey()
    #bovinos = models.ForeignKey()
    #jefes= models.ForeignKey()

    def __str__(self):
        if (self.cantidad):
            return self.cantidad