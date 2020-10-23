"""Usuarios views"""

#Django Rest Framework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

#Serializer
from apps.usuarios.serialize import UsuarioLoginSerializer

class UsuarioLoginAPIView(APIView):
    """Usuario login API View"""
    def post(self,request,*args,**kwargs):
        """manejar la solicitud de http POST"""
        serializer = UsuarioLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()
        data = {
            'status' : 'ok',
            'token' : token
        }
        return Response(data,status=status.HTTP_201_CREATED)
