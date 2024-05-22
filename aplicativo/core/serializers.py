from rest_framework import serializers
from .models import cliente

class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = ('nome', 'sobreNome')