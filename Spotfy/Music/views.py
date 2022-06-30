from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *


class QoshiqchilarAPIView(APIView):
    def get(self, request):
        qoshiqchilar = Qoshiqchi.objects.all()
        ser = QoshiqchiSerializer(qoshiqchilar, many=True)
        return Response(ser.data)
    def post(self,request):
        a = request.data
        ser = QoshiqchiSerializer(a)
        if ser.is_valid():
            ser.save()
        return(ser.data)




class QoshiqchiAPIView(APIView):
    def get(self,request, pk):
        # qoshiqchi = Qoshiqchi.objects.get(id=pk)
        qoshiqchi = get_object_or_404(Qoshiqchi, id=pk)
        ser = QoshiqchiSerializer(qoshiqchi)
        return Response(ser.data)
    def patch(self,request,pk):
        qoshiqchi = get_object_or_404(Qoshiqchi, id=pk)
        ser  = QoshiqchiSerializer(qoshiqchi,data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_202_ACCEPTED)
        return Response(ser.data, status.HTTP_406_NOT_ACCEPTABLE)
    def delete(self, request,pk):
        try:
            qoshiqchi = get_object_or_404(Qoshiqchi, id=pk).delete()
            data = {"xabar":"Muvaffaqiyatli o'chirildi!"}
            return  Response(data, status=status.HTTP_200_OK)
        except:
            data = {"xabar":"Bu id' da qo'shichi yo'q"}
            return Response(data, status=status.HTTP_404_NOT_FOUND)



class QoshiqAPIView(APIView):
    def get(self, request):
        qoshiqlar = Qoshiq.objects.all()
        ser = QoshiqchiSerializer(qoshiqlar, many=True)
        return Response(ser.data)
    def post(self,request):
        a = request.data
        ser = QoshiqSerializer(a)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

class AlbomlarAPIView(APIView):
    def get(self, request):
        albom = Albom.objects.all()
        ser = QoshiqchiSerializer(albom, many=True)
        return Response(ser.data)
    def post(self,request):
        a = request.data
        ser = AlbomSerializer(a)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


class AlbomAPIView(APIView):
    def get(self,request, pk):
        albom = get_object_or_404(Albom, id=pk)
        ser = AlbomSerializer(albom)
        return Response(ser.data)

    @action(diteal=True, methods=["get"])
    def qoshiqchilar(self, request, pk = None):
        albom = self.get_object()
        qoshiqchilar = Qoshiqchi.objects.filter(albom=albom)
        ser = AlbomSerializer(qoshiqchilar, many=True)
        return Response(ser.data)
    def patch(self,request,pk):
        albom = get_object_or_404(Albom, id=pk)
        ser  = AlbomSerializer(albom,data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_202_ACCEPTED)
        return Response(ser.data, status.HTTP_406_NOT_ACCEPTABLE)