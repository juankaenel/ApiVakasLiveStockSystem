"""Usuarios views"""

# Django Rest Framework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics

# Serializer
from apps.usuarios.models import Usuario
from apps.usuarios.serialize import UsuarioLoginSerializer, UsuarioModelSerializer, UsuarioSignUpSerializer


class UsuarioLoginAPIView(generics.GenericAPIView):
    """Usuario login API View"""

    serializer_class = UsuarioLoginSerializer

    # def post(self,request,*args,**kwargs):
    #     """manejar la solicitud de http POST"""
    #     serializer = UsuarioLoginSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     usuario, token = serializer.save()
    #     data = {
    #         'status' : UsuarioModelSerializer(usuario).data,
    #         'token' : token
    #     }
    #     return Response(data,status=status.HTTP_201_CREATED)


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        usuario = serializer.validated_data
        # kuser = UsuarioModelSerializer(Usuario, context=self.get_serializer_context()).data,
        # token = AuthToken.objects.create(user)[1]
        response = {
            #   "data": usuario[0],
            # "token": token
        }
        print(usuario)
        return Response(response)


class UsuarioSignUpAPIView(APIView):
    """Usuario signup API View"""

    def post(self, request, *args, **kwargs):
        """manejar la solicitud de http POST"""
        serializer = UsuarioSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        usuario = serializer.save()
        data = UsuarioModelSerializer(usuario).data
        return Response(data, status=status.HTTP_201_CREATED)
