# django rest
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# apps
from .models import Alimentos
from .serialize import AlimentosSerializer


# END POINTS
class AlimentosList(APIView):
    """
    Lista todas los alimentos, o crea uno nuevo.
    """

    def get(self, request, format=None):
        alimentos = Alimentos.objects.all()
        serializer = AlimentosSerializer(alimentos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AlimentosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlimentosDetail(APIView):
    """
    Recupera, actualiza o elimina una alimentación.
    """

    def get_object(self, pk):
        try:
            return Alimentos.objects.get(pk=pk)
        except Alimentos.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        alimento = self.get_object(pk)
        serializer = AlimentosSerializer(alimento)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        alimento = self.get_object(pk)
        serializer = AlimentosSerializer(alimento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        alimento = self.get_object(pk)
        alimento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)