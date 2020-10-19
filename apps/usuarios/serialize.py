from rest_framework import serializers
from .models import Usuario

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=60,min_length=6,write_only=True)

    class Meta:
        model = Usuario
        fields = ['email','username','password']

    def validate(self, attrs):
        email = attrs.get('email','')
        username = attrs.get('username','')

        if not username.isalnum():
            raise serializers.ValidationError('El nombre de usuario solo debe contener carácteres alfanuméricos')

        return attrs

    def create(self, validated_data):
        return Usuario.objects.create_user(**validated_data)