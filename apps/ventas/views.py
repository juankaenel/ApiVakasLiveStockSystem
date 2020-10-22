from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Ventas
from .serialize import VentasSerializer


# END POINTS
class VentasList(APIView):
    """
    Lista todas los ventas, o crea un nueva.
    """
    def get(self, request, format=None):
        ventas = Ventas.objects.all()
        serializer = VentasSerializer(ventas, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = VentasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VentasDetail(APIView):
    """
    Recupera, actualiza o elimina una venta.
    """
    def get_object(self, pk):
        try:
            return Ventas.objects.get(pk=pk)
        except Ventas.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        venta = self.get_object(pk)
        serializer = VentasSerializer(venta)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        venta = self.get_object(pk)
        serializer = VentasSerializer(venta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        venta = self.get_object(pk)
        venta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)