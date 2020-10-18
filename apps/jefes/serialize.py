from .models import Jefes
from rest_framework import serializers

# esta clase nos permitira transportar nuestros objetos a traves de la red por el protocolo http, ya sea formato json o otros
class JefesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jefes
        fields = '__all__'