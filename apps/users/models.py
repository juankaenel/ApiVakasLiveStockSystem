from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


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
            apellidos=apellidos
        )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario


class Usuario(AbstractBaseUser):
    """Modelo de perfil de usuarios.
       Modelo proxy, este extiende de la base de dato con otra informacion
       """
    # user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user')
    username = models.CharField('Nombre de usuario', max_length=255, unique=True, db_index=True)
    nombres = models.CharField('Nombres', max_length=255, db_index=True)
    apellidos = models.CharField('Apellidos', max_length=255, db_index=True)
    email = models.EmailField('Email', max_length=255, unique=True, db_index=True)
    dni = models.IntegerField('DNI', blank=True, null=True, unique=True)
    tipo = models.IntegerField('Tipo', blank=True, null=True)
    telefono = models.CharField('Teléfono', max_length=50, null=True, blank=True)
    # last_login = models.CharField(verbose_name='Último inicio',max_length=255)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    # is_staff = models.BooleanField(default=False)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombres', 'apellidos']


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
        :param self:
        :return:
        """
        return self.usuario_administrador
