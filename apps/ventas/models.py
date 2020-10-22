from django.db import models
from ..bovinos.models import Bovinos
from ..jefes.models import Jefes
from ..utils.models import Timestamps

class Ventas(Timestamps,models.Model):
    """
    Modelo Ventas
    """
    comprador = models.CharField(max_length=50,blank=False,null=False)
    descripcion = models.TextField(max_length=255)
    subtotal = models.FloatField(blank=False,null=False)
    iva = models.FloatField(blank=False,null=False)
    total = models.FloatField(blank=False,null=False)
    precio = models.FloatField(blank=False,null=False)
    establecimiento = models.CharField(blank=False,null=False,max_length=60)
    cantidad = models.IntegerField(blank=False,null=False)
    jefe = models.ForeignKey(Jefes,on_delete=models.CASCADE,blank=False,null=False)
    bovinos = models.ManyToManyField(Bovinos,db_table='VENTAS HAS BOVINOS',blank=False,) #relación muchos a muchos con bovinos, me creará una tabla intermedia

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'VENTA'
        ordering = ['id']
