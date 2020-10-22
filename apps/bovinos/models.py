from django.db import models

from ..categorias.models import Categorias
from ..jefes.models import Jefes
from ..razas.models import Razas
from ..utils.models import Timestamps

class Bovinos(Timestamps,models.Model):
    """
    Modelo Bovinos
    """
    numero_caravana = models.CharField('Número de Caravana',max_length=25)
    fecha_nacimiento = models.DateField('Fecha de nacimiento')
    peso_nacimiento = models.FloatField('Peso de nacimiento')
    ultimo_peso = models.FloatField('Último peso')
    observacion = models.TextField(max_length=255)
    sexo = models.CharField(max_length=45)
    vendido = models.BooleanField()
    jefe = models.ForeignKey(Jefes, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    raza = models.ForeignKey(Razas, on_delete=models.CASCADE)
    #foto

    def __str__(self):
        return self.numero_caravana

    class Meta:
        verbose_name = 'Bovino'
        verbose_name_plural = 'Bovinos'
        db_table = 'BOVINO'  # nombre de la tabla
        ordering = ['id']  # ordena por id de forma ascendente
