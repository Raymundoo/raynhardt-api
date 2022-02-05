# -*- coding: utf-8 -*-

import json
import requests
from django.utils import formats
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import MrOlimpyaSerializers
from .models import MrOlimpya
from .forms import AutorForm
from rest_framework import generics, status
from django.http import Http404
from rest_framework.renderers import JSONRenderer

    
class MrOlimpya_APIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None, *args, **kwargs):
        mr_olimpya = MrOlimpya.objects.all()
        serializer = MrOlimpyaSerializers(mr_olimpya, many=True)
        
        return Response(serializer.data)
    def mr_olimpya(self, request, format=None):
        serializer = MrOlimpyaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MrOlimpya_APIView_Detail(APIView):
    # permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return MrOlimpya.objects.get(pk=pk)
        except MrOlimpya.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        mr_olimpya = self.get_object(pk)
        serializer = MrOlimpyaSerializers(mr_olimpya)  
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        mr_olimpya = self.get_object(pk)
        serializer = MrOlimpyaSerializers(mr_olimpya, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        mr_olimpya = self.get_object(pk)
        mr_olimpya.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListCreateApiViewMrOlimpya(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = MrOlimpya.objects.all()
    serializer_class = MrOlimpyaSerializers
    renderer_classes = [JSONRenderer]


@login_required
def home(request):
     url = "http://127.0.0.1:8000/api/autores/"
     response = requests.get(url, timeout=5)
     object_list = []
     if response.status_code == 200:
         object_list = json.loads(response.content)
     return render(request, 'home/index.html', {"object_list": object_list})


def autor_add_api(request):

    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            data = json.dumps(form.cleaned_data)
            endpoint = "http://127.0.0.1:8000/api/autores/"
            response = requests.post(url=endpoint, data=data, timeout=5)
            print(response.status_code)
            if response.status_code == 201:
                print("OK")
                return redirect('autor_lista_api')
    else:
        form = AutorForm()
    
    return render(request, 'autor_form.html', {'form': form})


def autor_edit_api(request, id_autor):

    endpoint = "http://127.0.0.1:8000/api/autores/{id_autor}/".format(id_autor=id_autor)
    response = requests.get(url=endpoint, timeout=5)
    if response.status_code == 200:
        autor_api = json.loads(response.content)
    else:
        return redirect('autor_lista_api')


    if request.method == 'GET':
        form = AutorForm(initial=autor_api)
    else:
        form = AutorForm(request.POST)
        if form.is_valid():
            data = json.dumps(form.cleaned_data)
            response = requests.put(url=endpoint, data=data, timeout=5)
            return redirect('autor_lista_api')
    return render(request,'autor_form.html', {'form': form})


def autor_delete_api(request, id_autor):

    if request.method == 'POST':
        endpoint = "http://127.0.0.1:8000/api/autores/{id_autor}/".format(id_autor=id_autor)
        response = requests.delete(url=endpoint, timeout=5)
        if response.status_code == 204:
            print("OK")
            return redirect('autor_lista_api')
    else:
        endpoint = "http://127.0.0.1:8000/api/autores/{id_autor}/".format(id_autor=id_autor)
        response = requests.get(url=endpoint, timeout=5)
        if response.status_code == 200:
            autor = json.loads(response.content)
        else:
            return redirect('autor_lista_api')
    return render(request, 'autor_delete.html', {'autor': autor})