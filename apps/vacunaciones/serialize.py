from .models import Vacunaciones
from rest_framework import serializers

# esta clase nos permitira transportar nuestros objetos a traves de la red por el protocolo http, ya sea formato json o otros
class VacunacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacunaciones
        fields = '__all__'