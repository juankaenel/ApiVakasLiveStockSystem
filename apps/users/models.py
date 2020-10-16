from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    """Modelo de perfil de usuarios.
       Modelo proxy, este extiende de la base de dato con otra informacion
       """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #username = models.CharField(verbose_name='Nombre de usuario',max_length=255,unique=True,db_index=True)
    nombre = models.CharField(verbose_name='Nombre',max_length=255,db_index=True)
    email = models.EmailField(verbose_name='Email',max_length=255,unique=True,db_index=True)
    dni = models.IntegerField(verbose_name='DNI',blank=True,null=True,unique=True)
    tipo = models.IntegerField(verbose_name='Tipo', blank=True,null=True)
    telefono = models.CharField(verbose_name='Teléfono',max_length=50,null=True,blank=True)
    #last_login = models.CharField(verbose_name='Último inicio',max_length=255)
    #is_active = models.BooleanField(default=True)
    #is_admin = models.BooleanField(default=False)
    #is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return an username"""
        return self.user.username


