from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Compras
from .serialize import ComprasSerializer


# END POINTS
class ComprasList(APIView):
    """
    Lista todas los compras, o crea un nueva.
    """
    def get(self, request, format=None):
        compras = Compras.objects.all()
        serializer = ComprasSerializer(compras, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ComprasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ComprasDetail(APIView):
    """
    Recupera, actualiza o elimina una compra.
    """
    def get_object(self, pk):
        try:
            return Compras.objects.get(pk=pk)
        except Compras.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        compra = self.get_object(pk)
        serializer = ComprasSerializer(compra)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        compra = self.get_object(pk)
        serializer = ComprasSerializer(compra, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        compra = self.get_object(pk)
        compra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)