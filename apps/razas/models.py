from django.db import models
from ..utils.models import Timestamps

class Razas(Timestamps,models.Model):
    """
    Modelo Razas
    """
    nombre = models.CharField(max_length=40, null=False,blank=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Raza'
        verbose_name_plural = 'Razas'
        db_table = 'RAZA'
        ordering = ['id']
