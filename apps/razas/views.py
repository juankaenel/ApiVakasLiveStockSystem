from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Razas
from .serialize import RazasSerializer


# END POINTS
class RazasList(APIView):
    """
    Lista todas los razas, o crea una nueva.
    """
    def get(self, request, format=None):
        razas = Razas.objects.all()
        serializer = RazasSerializer(razas, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = RazasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RazasDetail(APIView):
    """
    Recupera, actualiza o elimina una raza.
    """
    def get_object(self, pk):
        try:
            return Razas.objects.get(pk=pk)
        except Razas.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        raza = self.get_object(pk)
        serializer = RazasSerializer(raza)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        raza = self.get_object(pk)
        serializer = RazasSerializer(raza, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        raza = self.get_object(pk)
        raza.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)