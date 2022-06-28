from django.shortcuts import render
# from .models import Monitors

from django.http import JsonResponse
from rest_framework import generics
from .serializers import MonitorsSerializer
from .models import Monitors

# Create your views here.


class MonitorsList(generics.ListCreateAPIView):
    queryset = Monitors.objects.all()
    serializer_class = MonitorsSerializer

