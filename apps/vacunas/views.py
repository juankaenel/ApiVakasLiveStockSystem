from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Vacunas
from .serialize import VacunasSerializer

# END POINTS
class VacunasList(APIView):
    """
    Lista todos las vacunas, o crea una nueva.
    """
    def get(self, request, format=None):
        vacunas = Vacunas.objects.all()
        serializer = VacunasSerializer(vacunas, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = VacunasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VacunasDetail(APIView):
    """
    Recupera, actualiza o elimina una vacuna.
    """
    def get_object(self, pk):
        try:
            return Vacunas.objects.get(pk=pk)
        except Vacunas.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        precipitacion = self.get_object(pk)
        serializer = VacunasSerializer(precipitacion)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        precipitacion = self.get_object(pk)
        serializer = VacunasSerializer(precipitacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        precipitacion = self.get_object(pk)
        precipitacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)