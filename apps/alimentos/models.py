from django.db import models
from ..utils.models import Timestamps

class Alimentos(Timestamps,models.Model):
    """
    Modelo Alimentos
    """
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=70)
    habilitado = models.SmallIntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Alimento'
        verbose_name_plural = 'Alimentos'
        db_table = 'ALIMENTO'  # nombre de la tabla
        ordering = ['id']