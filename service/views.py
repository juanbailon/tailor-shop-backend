from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import ServiceSerializer
from .models import Service

# Create your views here.
class CreateServiceView(generics.CreateAPIView):
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]

class UpdateServiceView(generics.UpdateAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    permission_classes = [permissions.AllowAny]
    lookup_field = 'pk'