from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from sitioVet.models import Mascota
from rest_api.serializers import MascotaSerializer


@csrf_exempt
@api_view(['GET', 'POST'])
def lista_mascotas(request):
    '''
    Lista de las mascotas
    '''
    if request.method == 'GET':
        mascotas = Mascota.objects.all()
        serial = MascotaSerializer(mascotas, many=True)
        return Response(serial.data)
    elif request.method == 'POST':
        serial = MascotaSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def mascota_id(request, id):
    '''
    Macota por ID
    '''
    try:
        mascota = Mascota.objects.get(idMascota=id)
    except Mascota.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serial = MascotaSerializer(mascota)
        return Response(serial.data)     
    elif request.method == 'PUT':
        serial = MascotaSerializer(mascota, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_304_NOT_MODIFIED)
    elif request.method == 'DELETE':
        mascota.delete()
        return Response(status=status.HTTP_200_OK)



