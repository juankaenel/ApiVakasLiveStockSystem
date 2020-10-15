from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Alimentaciones
from .serialize import AlimentacionSerializer


@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'index' : '/alimentaciones', #Get
        'store' : '/alimentaciones', #Post
        'show' : '/alimentaciones/<str:pk>', #Get
        'update': '/alimentaciones/<str:pk>', #Put,
        'destroy': '/alimentaciones/<str:pk>', #Delete
    }
    return Response(api_urls)

# END POINTS
@api_view(['GET','POST'])
def alimentacion_is(request): #is -> index, store
   if request.method == 'GET':
       alimentacion = Alimentaciones.objects.all()
       serializer = AlimentacionSerializer(alimentacion,many=True)

       return Response(serializer.data)
   elif request.method == 'POST':
       serializer = AlimentacionSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()

       return Response(serializer.data)

@api_view(['GET','DELETE','PUT'])
def alimentacion_sud(request,pk): #sud -> show, update, delete
   if request.method == 'GET':
       alimentacion = Alimentaciones.objects.get(id=pk)
       serializer = AlimentacionSerializer(alimentacion, many=False)
       return Response(serializer.data)
   elif request.method == 'PUT':
       alimentacion = Alimentaciones.objects.get(id=pk)
       serializer = AlimentacionSerializer(instance=alimentacion,data=request.data)
       if serializer.is_valid():
           serializer.save()
       return Response(serializer.data)
   elif request.method == 'DELETE':
       alimentacion = Alimentaciones.objects.get(id=pk)
       alimentacion.delete()
       return Response('Alimentación borrado con éxito!')