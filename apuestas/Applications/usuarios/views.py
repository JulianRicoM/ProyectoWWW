from django.shortcuts import render

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializer import usuariosSerializer
from .models import Usuarios

# Si el metodo es POST la funcion estapa un body de tipo Usuarios
# Si el  metodo es get la funcion retornará una lista de Usuarios
class UsersList(generics.ListCreateAPIView):
    serializer_class = usuariosSerializer
    queryset = Usuarios.objects.filter(is_active=True)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = usuariosSerializer(queryset, many=True)
        return Response(serializer.data)

# Si el metodo es GET espera un número de cedula y retornará el usuario
# Si el metodo es PUT espera un número de cedula con un cuerpo de tipo Usuario y actualizará el usuario
# Si el metodo es DELETE espera una cedula y eliminará el usuario 
@api_view(['GET', 'PUT', 'DELETE'])
def UserDetail(request, id):
    try:
        user = Usuarios.objects.get(documento=id)
    except Usuarios.DoesNotExist as e:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = usuariosSerializer(user, context={'request': request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    if request.method == 'DELETE':
        user.delete()
        return Response(
            {'message': 'El usuario fue eliminado satisfactoriamente'},
            status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        serializer = usuariosSerializer(
            user, data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(
            {
                'detail': serializer.errors,
                'data': 'Ha ocurrido un error por favor revise los datos'
            },
            status=status.HTTP_404_NOT_FOUND)
