#django
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver
#django_rest
from rest_framework.authtoken.models import Token
#apps
from config import settings
from ..utils.models import Timestamps

class UsuarioManager(BaseUserManager):
    def create_user(self, username, nombres, apellidos, email, password=None):
        if not email:
            raise ValueError('El usuario debe tener email')

        # hago referencia al usuario del modelo

        usuario = self.model(  # usuario = Usuario
            username=username,
            email=self.normalize_email(email),
            nombres=nombres,
            apellidos=apellidos
        )

        usuario.set_password(password)  # encripta la contraseña
        usuario.save()
        return usuario

    def create_superuser(self, username, nombres, apellidos, email, password):
        usuario = self.create_user(
            email=email,
            username=username,
            nombres=nombres,
            apellidos=apellidos,
            password=password
        )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario


#TIPO_USUARIO = (1,'Jefe',2,'Empleado')

class Usuario(Timestamps,AbstractBaseUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user')
    username = models.CharField('Nombre de usuario', max_length=255, unique=True, db_index=True)
    nombres = models.CharField('Nombres', max_length=255, db_index=True)
    apellidos = models.CharField('Apellidos', max_length=255, db_index=True)
    email = models.EmailField('Email', max_length=255, unique=True, db_index=True)
    dni = models.IntegerField('DNI', blank=True, null=True, unique=True)
    tipo = models.IntegerField('Tipo',blank=True, null=True)
    telefono = models.CharField('Teléfono', max_length=50, null=True, blank=True)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    usuario_verificado = models.BooleanField(default=False)
    objects = UsuarioManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        """Return an username"""
        return f'{self.nombres},{self.apellidos}'


    def has_perm(self, perm, obj=None):
        return True


    def has_module_perms(self, app_label):
        return True


    @property
    def is_staff(self):
        """
        Verifica y valida si un usuario es admin o no
        """
        return self.usuario_administrador

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'USUARIO'  # nombre de la tabla
        ordering = ['id']  # ordena por id de forma ascendente

#creación del token para el usuario
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)