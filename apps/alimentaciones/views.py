#django rest
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
#apps
from .models import Alimentaciones
from .serialize import AlimentacionSerializer

# END POINTS
class AlimentacionesList(APIView):
    """
    Lista todas los alimentaciones, o crea una nueva.
    """
    def get(self, request, format=None):
        alimentaciones = Alimentaciones.objects.all()
        serializer = AlimentacionSerializer(alimentaciones, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = AlimentacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AlimentacionesDetail(APIView):
    """
    Recupera, actualiza o elimina una alimentación.
    """
    def get_object(self, pk):
        try:
            return Alimentaciones.objects.get(pk=pk)
        except Alimentaciones.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        alimentacion = self.get_object(pk)
        serializer = AlimentacionSerializer(alimentacion)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        alimentacion = self.get_object(pk)
        serializer = AlimentacionSerializer(alimentacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        alimentacion = self.get_object(pk)
        alimentacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
