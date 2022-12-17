from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Estado, TipoApuesta, Apuesta
from .serializer import listaApuestaSerializer, apuestaSerializer, estadoSerializer, tipoApuestaSerializer

# Si el metodo es POST la funcion espera un body de tipo Estado
# Si el  metodo es GET la funcion retornará una lista de Estados
class EstatusList(generics.ListCreateAPIView ):
    serializer_class = estadoSerializer
    queryset = Estado.objects.all()
    
    def List(self, request):
        queryset = self.get_queryset()
        serializer = estadoSerializer(queryset, many = True)
        return Response(serializer.data)

# Si el metodo es POST la funcion espera un body de tipo TipoApuesta
# Si el  metodo es GET la funcion retornará una lista de TipoApuesta
class BetTypeList(generics.ListCreateAPIView ):
    serializer_class = tipoApuestaSerializer
    queryset = TipoApuesta.objects.all()
    
    def List(self, request):
        queryset = self.get_queryset()
        serializer = tipoApuestaSerializer(queryset, many = True)
        return Response(serializer.data)
    
# Solo el metodo GET esta permitido, la funcion retornará una lista de Apuestas
@api_view(['GET'])
def BetList(request):
    queryset = Apuesta.objects.filter(is_active=True)
    serializer = listaApuestaSerializer(queryset, many=True)
    return Response(serializer.data)

# Solo esta permitido el metodo POST la funcion espera un body de tipo Apuesta y crea la apuesta
@api_view(['POST'])
def CreateBet(request):
    serializer = apuestaSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    return Response(
        {
            "detail": serializer.errors,
            "data": "Ha ocurrido un error, por favor revise los datos.",
        },
        status=status.HTTP_400_BAD_REQUEST,
    )

# Si el metodo es GET espera el id de la apuesta y retornará los datos de la apuesta
# Si el metodo es PUT espera el id de la apuesta con un cuerpo de tipo Apuesta y actualizará la apuesta
# Si el metodo es DELETE espera el id dela apuesta y eliminará la apuesta 
@api_view(['GET', 'PUT', 'DELETE'])
def BetDetail(request, id):
    try:
        match = Apuesta.objects.get(pk=id)
    except Apuesta.DoesNotExist as e:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = apuestaSerializer(match, context={'request': request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    if request.method == 'DELETE':
        match.delete()
        return Response(
            {'message': 'La apuesta fue eliminada satisfactoriamente'},
            status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        serializer = apuestaSerializer(
            match, data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(
            {
                'detail': serializer.errors,
                'data': 'Ha ocurrido un error por favor revise los datos'
            },
            status=status.HTTP_404_NOT_FOUND)


