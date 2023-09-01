from django.shortcuts import render
from .models import Singer,Song
from .serializers import SingerSerializer,SongSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.generics import ListAPIView


class Singerdetail(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    
class Songdetail(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    
