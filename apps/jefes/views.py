from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Jefes
from .serialize import JefesSerializer


# END POINTS
class JefesList(APIView):
    """
    Lista todos los Jefes, o crea un nuevo Jefe.
    """
    def get(self, request, format=None):
        jefes = Jefes.objects.all()
        serializer = JefesSerializer(jefes, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = JefesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JefesDetail(APIView):
    """
    Recupera, actualiza o elimina un jefe.
    """
    def get_object(self, pk):
        try:
            return Jefes.objects.get(pk=pk)
        except Jefes.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        jefe = self.get_object(pk)
        serializer = JefesSerializer(jefe)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        jefe = self.get_object(pk)
        serializer = JefesSerializer(jefe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        jefe = self.get_object(pk)
        jefe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)