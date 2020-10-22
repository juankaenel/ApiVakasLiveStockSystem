from .models import Razas
from rest_framework import serializers

class RazasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Razas
        fields = '__all__'