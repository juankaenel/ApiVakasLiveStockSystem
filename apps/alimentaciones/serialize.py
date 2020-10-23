from .models import Alimentaciones
from rest_framework import serializers

class AlimentacionSerializer(serializers.ModelSerializer):
    """
        AlimentacionSerializer: esta clase nos permitira transportar nuestros objetos a traves de la red por el protocolo http, ya sea formato json o otros

        La ModelSerializer clase proporciona un atajo que le permite crear automáticamente una
        Serializer clase con campos que corresponden a los campos del Modelo.

        La ModelSerializerclase es la misma que una Serializerclase regular , excepto que :

        Generará automáticamente un conjunto de campos para usted, según el modelo.
        Generará automáticamente validadores para el serializador, como validadores unique_together.
        Incluye implementaciones simples predeterminadas de .create()y .update().

        Para inspeccionar el serializer de Alimentación sigo estos pasos:

        abra el shell de Django, use python manage.py shell, luego importe la clase del serializador,
        cree una instancia e imprima la representación del objeto ...

        from apps.compras.serialize import ComprasSerializer
        serializer = ComprasSerializer()
        print(serializer)
        """
    class Meta:
        model = Alimentaciones
        fields = '__all__'