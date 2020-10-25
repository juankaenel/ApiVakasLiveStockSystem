"""Serializer Usuario"""

#Django
from django.contrib.auth import authenticate,password_validation

#Django Rest Framework
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
#local
from apps.usuarios.models import Usuario, UsuarioManager


class UsuarioModelSerializer(serializers.ModelSerializer):
    """User model serializer"""

    class Meta:
        """Meta class"""
        model = Usuario
        fields = '__all__'

class RegistroSerializer(serializers.Serializer):
    """Usuario sign up serializer

    Maneja los datos de validación y creación de usuarios
    """
    email = serializers.EmailField(validators=[
        UniqueValidator(queryset=Usuario.objects.all()) #valido que solo hay un único email
    ])
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=Usuario.objects.all())]
    )
    password = serializers.CharField(min_length=8, max_length=64)
    #password_confirmation = serializers.CharField(min_length=8, max_length=64)
    nombres = serializers.CharField(min_length=2, max_length=30)
    apellidos = serializers.CharField(min_length=2, max_length=30)

    #def validate(self, data):
    #    """Verifica que haya coincidencia de passwords"""
    #    passwd = data.get('password')
    #    passwd_conf = data.get('password_confirmation')
    #    if passwd != passwd_conf:
    #        raise serializers.ValidationError("Las contraseñas no coinciden")
    #    #password_validation.validate_password(passwd)
    #    return data

    def create(self, data):
        #data.pop('password_confirmation') #eliminamos el password confirmation
        usuario = Usuario.objects.create(**data)
        return usuario


#class UsuarioLoginSerializer(serializers.Serializer):
#   """Usario login serializer

#   Maneja la data request de login
#   """

#   email = serializers.EmailField()
#   password = serializers.CharField(min_length=8, max_length=64)

#   def validate(self, data):
#       """Verifica credenciales"""
#       usuario = authenticate(**data)
#       print(usuario)
#       if not usuario:
#           raise serializers.ValidationError('Credenciales inválidas')
#       return data



#class RegistroSerializer(serializers.Serializer):
#    username = serializers.CharField()
#    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
#
#    def validate(self, data):
#        email =data.get('email','')
#        username =data.get('username','')
#
#        if not username.isalnum():
#            raise serializers.ValidationError('El nombre de usuario debe contener caracteres alfanuméricos')
#        return data
#
#    def create(self, validated_data):
#        return Usuario.objects.create_user(**validated_data)