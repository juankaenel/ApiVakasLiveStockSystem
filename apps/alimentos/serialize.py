from .models import Alimentos
from rest_framework import serializers

# esta clase nos permitira transportar nuestros objetos a traves de la red por el protocolo http, ya sea formato json o otros
class AlimentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimentos
        fields = '__all__'