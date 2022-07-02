from django.shortcuts import render
# from .models import Monitors

from django.http import JsonResponse
from rest_framework import generics
from .serializers import MonitorsSerializer, KeyboardsSerializer, MousesSerializer, HeadPhonesSerializer
from .models import Monitors, KeyBoard, Mouse, HeadPhone

# Create your views here.

#Monitors 
class MonitorsList(generics.ListCreateAPIView):
    queryset = Monitors.objects.all()
    serializer_class = MonitorsSerializer

class MonitorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Monitors.objects.all()
    serializer_class = MonitorsSerializer


#Keyboards
class KeyboardsList(generics.ListCreateAPIView):
    queryset = KeyBoard.objects.all()
    serializer_class = KeyboardsSerializer

class KeyboardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = KeyBoard.objects.all()
    serializer_class = KeyboardsSerializer


#Mouses
class MousesList(generics.ListCreateAPIView):
    queryset = Mouse.objects.all()
    serializer_class = MousesSerializer


#Headphones
class HeadPhonesList(generics.ListCreateAPIView):
    queryset = HeadPhone.objects.all()
    serializer_class = HeadPhonesSerializer





