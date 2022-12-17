from rest_framework import serializers
from .models import Partidos, Resultado

class partidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partidos
        exclude = ["is_active"]

class resultadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resultado
        fields = '__all__'
        
class listaPartidoSerializer(serializers.ModelSerializer):
    resultado = resultadoSerializer()
    class Meta:
        model = Partidos
        exclude = ["is_active"]