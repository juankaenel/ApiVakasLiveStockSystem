"""Usuarios views"""

# Django Rest Framework
import jwt
from django.urls import reverse
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework_simplejwt.tokens import RefreshToken

#django
from django.contrib.sites.shortcuts import get_current_site

#apps
from apps.usuarios.models import Usuario
from apps.usuarios.serialize import UsuarioModelSerializer, RegistroSerializer
from apps.usuarios.utils import Utils
from config import settings


class RegistroUsuario(generics.GenericAPIView):
    serializer_class = RegistroSerializer

    def post(self,request):
        usuario = request.data
        serializer = self.serializer_class(data=usuario)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        usuario_data = serializer.data

        usuario = Usuario.objects.get(email=usuario_data['email']) #obtengo el email del usuario del cual quiere realizar el registro
        token = RefreshToken.for_user(usuario).access_token #genera un token para el email correspondiente

        current_site = get_current_site(request).domain
        relativeLink = reverse('verificar-email') #retorna a la ruta de verificación de email
        absurl = 'http://'+current_site+relativeLink+"?token="+str(token) #absurl-> ruta absoluta
        email_body = 'Hola '+ usuario.username + 'usá este link para verificar tu email \n' + absurl
        data = {'email_body':email_body,'to_email':usuario.email,'email_subject':'Verifica tu email'}

        Utils.send_email(data) #llamo a la función para eniar el email

        return Response(usuario_data, status=status.HTTP_201_CREATED)

class VerificarEmail(generics.GenericAPIView):
    def get(self,request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token,settings.SECRET_KEY)
            usuario = Usuario.objects.get(id=payload['usuario_id'])
            if not usuario.usuario_verificado: #controlo si ya está verificado el usr
                usuario.usuario_verificado = True  # verifico el usuario
                usuario.save()
            return Response({'email':'Activado satisfactoriamente'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error':'Activación expirada'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Token inválido'}, status=status.HTTP_400_BAD_REQUEST)
