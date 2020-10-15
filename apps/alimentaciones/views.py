from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Alimentaciones
from .serialize import AlimentacionesSerializer

#esta clase me permite realizar el crud
# class AlimentacionesViewSet(viewsets.ModelViewSet):
#     queryset = Alimentaciones.objects.all()
#     serializer_class = AlimentacionesSerializer

@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'index' : '/alimentaciones',
        'store' : '/alimentaciones', #create
        'show' : '/alimentaciones/<str:pk>',
        'update': '/alimentaciones/<str:pk>',
        'destroy': '/alimentaciones/<str:pk>',
    }
    return Response(api_urls)


@api_view(['GET'])
def index(request):
    alimentaciones = Alimentaciones.objects.all()
    serializer = AlimentacionesSerializer(alimentaciones,many=True)
    return Response(serializer.data)