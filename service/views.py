from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import CreateServiceSerializer, UpdateServiceSerializer
from .models import Service

# Create your views here.
class CreateServiceView(generics.CreateAPIView):
    serializer_class = CreateServiceSerializer
    permission_classes = [permissions.AllowAny]

class UpdateServiceView(generics.UpdateAPIView):
    serializer_class = UpdateServiceSerializer
    queryset = Service.objects.all()
    permission_classes = [permissions.AllowAny]
    lookup_field = 'pk'