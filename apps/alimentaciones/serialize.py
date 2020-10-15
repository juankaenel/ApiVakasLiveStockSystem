from .models import Alimentaciones
from rest_framework import serializers

# esta clase nos permitira transportar nuestros objetos a traves de la red por el protocolo http, ya sea formato json o otros
class AlimentacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimentaciones
        fields = '__all__'