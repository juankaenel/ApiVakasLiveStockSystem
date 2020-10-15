from rest_framework import viewsets
from .models import Alimentos
from .serialize import AlimentosSerializer

#esta clase me permite realizar el crud
class AlimentosViewSet(viewsets.ModelViewSet):
    queryset = Alimentos.objects.all()
    serializer_class = AlimentosSerializer