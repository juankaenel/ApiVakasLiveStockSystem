from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Precipitaciones
from .serialize import PrecipitacionesSerializer


# END POINTS
class PrecipitacionesList(APIView):
    """
    Lista todos las precipitaciones, o crea una nueva.
    """
    def get(self, request, format=None):
        precipitaciones = Precipitaciones.objects.all()
        serializer = PrecipitacionesSerializer(precipitaciones, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = PrecipitacionesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PrecipitacionesDetail(APIView):
    """
    Recupera, actualiza o elimina una precipitacion.
    """
    def get_object(self, pk):
        try:
            return Precipitaciones.objects.get(pk=pk)
        except Precipitaciones.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        precipitacion = self.get_object(pk)
        serializer = PrecipitacionesSerializer(precipitacion)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        precipitacion = self.get_object(pk)
        serializer = PrecipitacionesSerializer(precipitacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        precipitacion = self.get_object(pk)
        precipitacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)