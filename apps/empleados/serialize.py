from .models import Empleados
from rest_framework import serializers

# esta clase nos permitira transportar nuestros objetos a traves de la red por el protocolo http, ya sea formato json o otros
class EmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = '__all__'