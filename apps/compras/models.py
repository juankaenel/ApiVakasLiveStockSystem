from django.db import models
from ..bovinos.models import Bovinos
from ..utils.models import Timestamps

class Compras(Timestamps,models.Model):
    """
    Modelo Compras
    """
    comprador = models.CharField(max_length=50,blank=False)
    descripcion = models.TextField(max_length=255)
    subtotal = models.FloatField(blank=False)
    iva = models.FloatField(blank=False)
    total = models.FloatField(blank=False)
    precio = models.FloatField(blank=False)
    establecimiento = models.CharField(blank=False,max_length=60)
    cantidad = models.IntegerField(blank=False)
    bovinos = models.ManyToManyField(Bovinos,db_table='COMPRAS HAS BOVINOS',blank=False,) #relación muchos a muchos con bovinos, me creará una tabla intermedia

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        db_table = 'COMPRA'
        ordering = ['id']
