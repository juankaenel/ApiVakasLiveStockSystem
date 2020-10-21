from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Vacunaciones
from .serialize import VacunacionesSerializer

# END POINTS
class VacunacionesList(APIView):
    """
    Lista todos las vacunaciones, o crea una nueva.
    """
    def get(self, request, format=None):
        vacunacion = Vacunaciones.objects.all()
        serializer = VacunacionesSerializer(vacunacion, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = VacunacionesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VacunacionesDetail(APIView):
    """
    Recupera, actualiza o elimina una vacunación.
    """
    def get_object(self, pk):
        try:
            return Vacunaciones.objects.get(pk=pk)
        except Vacunaciones.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        vacunacion = self.get_object(pk)
        serializer = VacunacionesSerializer(vacunacion)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        vacunacion = self.get_object(pk)
        serializer = VacunacionesSerializer(vacunacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        vacunacion = self.get_object(pk)
        vacunacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)