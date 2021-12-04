from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MrOlimpyaSerializers
from .models import MrOlimpya
from rest_framework import status
from django.http import Http404
    
class MrOlimpya_APIView(APIView):
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