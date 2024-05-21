from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import ServiceRawMaterialSerializer
from .models import ServiceRawMaterial

# Create your views here.
class RegisterServiceRawMaterialView(generics.CreateAPIView):
    serializer_class = ServiceRawMaterialSerializer
    permission_classes = [permissions.IsAuthenticated]