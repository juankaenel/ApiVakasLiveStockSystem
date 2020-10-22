from django.db import models
from ..utils.models import Timestamps

class Categorias(Timestamps,models.Model):
    """
    Modelo Categorias
    """
    nombre = models.CharField(max_length=40, null=False,blank=False)
    edad_inicial = models.IntegerField('Edad inicial', null=False,blank=False)
    edad_final = models.IntegerField('Edad final', null=False,blank=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'CATEGORIA'
        ordering = ['id']
