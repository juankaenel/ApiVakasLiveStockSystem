"""Serializer Usuario"""

#Django
from django.contrib.auth import authenticate

#Django Rest Framework
from rest_framework import serializers

class UsuarioLoginSerializer(serializers.Serializer):
    """Usario login serializer

    Maneja la data request de login
    """

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Verifica credenciales"""
        usuario = authenticate(username=data['email'],password=data['password'])
        if not usuario:
            raise serializers.ValidationError('Credenciales inválidas')
        return data


