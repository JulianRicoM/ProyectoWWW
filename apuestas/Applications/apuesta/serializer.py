from rest_framework import serializers

from .models import Estado, TipoApuesta, Apuesta
from Applications.partidos.serializer import listaPartidoSerializer
from Applications.usuarios.serializer import usuariosSerializer
class estadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'
        
class tipoApuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoApuesta
        fields = '__all__'
        
class listaApuestaSerializer(serializers.ModelSerializer):
    usuario = usuariosSerializer
    partido =  listaPartidoSerializer()
    tipo_apuesta =  tipoApuestaSerializer()
    estado = estadoSerializer()
    class Meta:
        model = Apuesta
        exclude = ['is_active']
        
class apuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apuesta
        exclude = ['is_active']