import json
import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from mascotas.models import Mascota
from mascotas.serializer import MascotaSerializer

# DRF
from rest_framework import generics, status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class ListCreateApiViewMascota(generics.ListAPIView):

    permission_classes = [IsAuthenticated]
    queryset = Mascota.objects.select_related("persona").prefetch_related("vacunas").all()
    serializer_class = MascotaSerializer
    renderer_classes = [JSONRenderer]


class MascotaAPIViewDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Mascota.objects.get(pk=pk)
        except Mascota.DoesNotExist:
            raise Mascota

    def get(self, request, pk, format=None):
        mr_olimpya = self.get_object(pk)
        serializer = MascotaSerializer(mr_olimpya)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        mr_olimpya = self.get_object(pk)
        serializer = MascotaSerializer(mr_olimpya, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        mr_olimpya = self.get_object(pk)
        mr_olimpya.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@login_required
def mascota_lista_api(request):

    endpoint = "http://raynhardtapi.net:8000/v1/mascota/"
    response = requests.get(url=endpoint, cookies=request.COOKIES, timeout=5)
    object_list = []
    if response.status_code == 200:
        object_list = json.loads(response.content).get("results")

    datos = {'object_list': object_list, }
    return render(request, 'mascotas_list_api.html', datos)
