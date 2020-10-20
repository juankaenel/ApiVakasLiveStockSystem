from datetime import datetime
from django.db import models

from ..empleados.models import Empleados
from ..jefes.models import Jefes
from ..utils.models import Timestamps


class Precipitaciones(Timestamps, models.Model):
    """
    Modelo Precipitaciones
    """
    milimetraje = models.FloatField('Milimetrajes', max_length=45)
    fecha = models.DateField('Fecha de precipitación', default=datetime.now, null=False)
    jefes = models.ForeignKey(Jefes, on_delete=models.CASCADE, blank=True, null=True)
    empleados = models.ForeignKey(Empleados, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Precipitación'
        verbose_name_plural = 'Precipitaciones'

    def __str__(self):
        return f'Cantidad de milímetros registrados: {self.milimetraje}'
