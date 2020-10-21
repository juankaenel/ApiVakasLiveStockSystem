from .models import Vacunas
from rest_framework import serializers

# esta clase nos permitira transportar nuestros objetos a traves de la red por el protocolo http, ya sea formato json o otros
class VacunasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacunas
        fields = '__all__'