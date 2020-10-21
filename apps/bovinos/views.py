from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Bovinos
from .serialize import BovinosSerializer


# END POINTS
class BovinosList(APIView):
    """
    Lista todos los bovinos, o crea uno nueva.
    """
    def get(self, request, format=None):
        bovinos = Bovinos.objects.all()
        serializer = BovinosSerializer(bovinos, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = BovinosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BovinosDetail(APIView):
    """
    Recupera, actualiza o elimina un bovino.
    """
    def get_object(self, pk):
        try:
            return Bovinos.objects.get(pk=pk)
        except Bovinos.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bovino = self.get_object(pk)
        serializer = BovinosSerializer(bovino)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        bovino = self.get_object(pk)
        serializer = BovinosSerializer(bovino, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        bovino = self.get_object(pk)
        bovino.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
