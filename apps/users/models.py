from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import (BaseUserManager,PermissionsMixin)
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if username is None:
            raise TypeError('El usuario debería tener un nombre de usuario')
        if email is None:
            raise TypeError('El usuario debería tener un email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

    def create_superuser(self,username, email, password=None):
        if password == None:
            raise TypeError('El super usario debe llevar contraseña')

        user = self.create_user(username,email,password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name='Nombre de usuario',max_length=255,unique=True,db_index=True)
    email = models.EmailField(verbose_name='Email',max_length=255,unique=True,db_index=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = 'username'

    def __str__(self):
        return self.email

    def tokens(self):
        return ''


