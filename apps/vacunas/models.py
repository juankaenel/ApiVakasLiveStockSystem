from django.db import models
from ..utils.models import Timestamps

class Vacunas(Timestamps,models.Model):
    """
    Modelo Vacunas
    """
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=70)
    habilitado = models.SmallIntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Vacuna'
        verbose_name_plural = 'Vacunas'
        db_table = 'VACUNA'  # nombre de la tabla
        ordering = ['id']  # ordena por id de forma ascendente

