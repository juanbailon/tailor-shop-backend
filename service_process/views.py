from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import ServiceProcessSerializer
from .models import ServiceProcess

# Create your views here.

class RegisterServiceProcess(generics.CreateAPIView):
    serializer_class = ServiceProcessSerializer
    permission_classes = [permissions.IsAuthenticated]