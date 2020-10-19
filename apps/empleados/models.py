from django.db import models
from apps.usuarios.models import Usuario
from ..utils.models import Timestamps

class Empleados(Timestamps,models.Model):
    """
    Modelo Jefes
    """
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'