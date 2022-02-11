from django.shortcuts import render
from rest_framework import viewsets
from .serializers import VillainSerializer
from .models import Villain

# Create your views here.
class VillainViewset(viewsets.ModelViewSet):
    queryset = Villain.objects.all().order_by('name')
    serializer_class = VillainSerializer
    