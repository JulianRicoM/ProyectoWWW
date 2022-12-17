from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializer import partidoSerializer, resultadoSerializer, listaPartidoSerializer
from .models import Resultado, Partidos

# Si el metodo es POST la funcion espera un body de tipo Partido
# Si el  metodo es get la funcion retornará una lista de Partidos
class ResultList(generics.ListCreateAPIView ):
    serializer_class = resultadoSerializer
    queryset = Resultado.objects.all()
    
    def List(self, request):
        queryset = self.get_queryset()
        serializer = resultadoSerializer(queryset, many = True)
        return Response(serializer.data)


# Solo el metodo GET esta permitido, la funcion retornará una lista de Partidos
@api_view(['GET'])
def MatchList(request):
    queryset = Partidos.objects.filter(is_active=True)
    serializer = listaPartidoSerializer(queryset, many=True)
    return Response(serializer.data)

# Solo esta permitido el metodo POST la funcion espera un body de tipo Partido y crea el encuentro
@api_view(['POST'])
def CreateMatch(request):
    serializer = partidoSerializer(data=request.data)

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
# Si el metodo es GET espera el id del encuentr y retornará los datos del partido
# Si el metodo es PUT espera el id del encuentro con un cuerpo de tipo Partido y actualizará el encuentro
# Si el metodo es DELETE espera el id del enceuntro y eliminará el partido 
@api_view(['GET', 'PUT', 'DELETE'])
def MatchDetail(request, id):
    try:
        match = Partidos.objects.get(pk=id)
    except Partidos.DoesNotExist as e:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = partidoSerializer(match, context={'request': request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    if request.method == 'DELETE':
        match.delete()
        return Response(
            {'message': 'El Partido fue eliminado satisfactoriamente'},
            status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        serializer = partidoSerializer(
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
