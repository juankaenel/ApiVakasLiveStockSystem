from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Categorias
from .serialize import CategoriasSerializer


# END POINTS
class CategoriasList(APIView):
    """
    Lista todas los categorias, o crea una nueva.
    """
    def get(self, request, format=None):
        categorias = Categorias.objects.all()
        serializer = CategoriasSerializer(categorias, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = CategoriasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriasDetail(APIView):
    """
    Recupera, actualiza o elimina una categoria.
    """
    def get_object(self, pk):
        try:
            return Categorias.objects.get(pk=pk)
        except Categorias.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        categoria = self.get_object(pk)
        serializer = CategoriasSerializer(categoria)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        categoria = self.get_object(pk)
        serializer = CategoriasSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        categoria = self.get_object(pk)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)