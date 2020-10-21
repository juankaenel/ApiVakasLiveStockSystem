from django.db import models
from ..utils.models import Timestamps
from ..vacunas.models import Vacunas


class Vacunaciones(Timestamps,models.Model):
    """
    Modelo Vacunaciones
    """
    dosis = models.FloatField()
    descripcion = models.TextField(max_length=255,default='')
    periodo = models.CharField('Primero o segundo',max_length = 20)
    cantidad = models.CharField('Parcial o total',max_length=12) #se hará la validación a través de los enums del frontend
    modo_se = models.CharField('Modo de aplicación, sistemática o estratégica',max_length=20)  #se hará la validación a través de los enums del frontend
    vacuna = models.ForeignKey(Vacunas, on_delete=models.CASCADE)
    #bovino = models.ForeignKey(Bovinos, on_delete=models.CASCADE)

    def __str__(self):
        return self.vacuna.nombre

    class Meta:
        verbose_name = 'Vacunación'
        verbose_name_plural = 'Vacunaciones'
        db_table = 'VACUNACIONES'  # nombre de la tabla
        ordering = ['id']  # ordena por id de forma ascendente
