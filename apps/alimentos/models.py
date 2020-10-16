from django.db import models


class Alimentos(models.Model):
    """
    Modelo Alimentos
    """
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=70)
    habilitado = models.SmallIntegerField()

    def __str__(self):
        return self.nombre
