from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Empleados
from .serialize import EmpleadosSerializer


# END POINTS
class EmpleadosList(APIView):
    """
    Lista todos los Empleados, o crea uno nuevo.
    """
    def get(self, request, format=None):
        empleados = Empleados.objects.all()
        serializer = EmpleadosSerializer(empleados, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = EmpleadosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmpleadosDetail(APIView):
    """
    Recupera, actualiza o elimina un empleado.
    """
    def get_object(self, pk):
        try:
            return Empleados.objects.get(pk=pk)
        except Empleados.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        empleado = self.get_object(pk)
        serializer = EmpleadosSerializer(empleado)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        empleado = self.get_object(pk)
        serializer = EmpleadosSerializer(empleado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        empleado = self.get_object(pk)
        empleado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)