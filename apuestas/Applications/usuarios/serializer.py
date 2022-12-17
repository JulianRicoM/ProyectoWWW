from rest_framework import serializers

from Applications.usuarios.models import Usuarios 

class usuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        exclude = ["is_active"]