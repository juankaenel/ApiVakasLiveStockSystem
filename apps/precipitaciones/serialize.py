from .models import Precipitaciones
from rest_framework import serializers

# esta clase nos permitira transportar nuestros objetos a traves de la red por el protocolo http, ya sea formato json o otros
class PrecipitacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Precipitaciones
        fields = '__all__'