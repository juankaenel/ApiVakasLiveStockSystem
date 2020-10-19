from django.db import models
from apps.alimentos.models import Alimentos
from apps.jefes.models import Jefes
from apps.empleados.models import Empleados
from ..utils.models import Timestamps

class Alimentaciones(Timestamps,models.Model):
    """
    Modelo alimentaciones
    """
    cantidad = models.IntegerField()
    descripcion = models.TextField(default='', blank=True)
    #bovinos = models.ForeignKey()
    jefes= models.ForeignKey(Jefes,on_delete=models.CASCADE)
    empleados = models.ForeignKey(Empleados,on_delete=models.CASCADE)
    alimentos = models.ForeignKey(Alimentos, on_delete=models.CASCADE)

    #def __str__(self):
    #    if (self.cantidad):
    #        return self.cantidad

    class Meta:
        verbose_name = 'Alimentacion'
        verbose_name_plural = 'Alimentaciones'