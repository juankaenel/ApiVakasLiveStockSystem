from .models import Bovinos
from rest_framework import serializers

# esta clase nos permitira transportar nuestros objetos a traves de la red por el protocolo http, ya sea formato json o otros
class BovinosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bovinos
        fields = '__all__'