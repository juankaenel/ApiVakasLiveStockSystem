from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Alimentos
from .serialize import AlimentosSerializer


@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'index' : '/alimentos', #Get
        'store' : '/alimentos', #Post
        'show' : '/alimentos/<str:pk>', #Get
        'update': '/alimentos/<str:pk>', #Put,
        'destroy': '/alimentos/<str:pk>', #Delete
    }
    return Response(api_urls)

# END POINTS
@api_view(['GET','POST'])
def alimento_is(request): #is -> index, store
   if request.method == 'GET':
       alimento = Alimentos.objects.all()
       serializer = AlimentosSerializer(alimento,many=True)
       return Response(serializer.data)
   elif request.method == 'POST':
       serializer = AlimentosSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
       return Response(serializer.data)

@api_view(['GET','DELETE','PUT'])
def alimento_sud(request,pk): #sud -> show, update, delete
   if request.method == 'GET':
       alimento = Alimentos.objects.get(id=pk)
       serializer = AlimentosSerializer(alimento, many=False)
       return Response(serializer.data)
   elif request.method == 'PUT':
       alimento = Alimentos.objects.get(id=pk)
       serializer = AlimentosSerializer(instance=alimento,data=request.data)
       if serializer.is_valid():
           serializer.save()
       return Response(serializer.data)
   elif request.method == 'DELETE':
       alimento = Alimentos.objects.get(id=pk)
       alimento.delete()
       return Response('Alimento borrado con éxito!')