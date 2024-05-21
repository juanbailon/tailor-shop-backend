from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import ServiceProcessSerializer
from .models import ServiceProcess


class RegisterServiceProcess(generics.CreateAPIView):
    serializer_class = ServiceProcessSerializer
    permission_classes = [permissions.IsAuthenticated]


class ListServiceProcessView(generics.ListAPIView):
    serializer_class = ServiceProcess
    permission_classes = [permissions.IsAuthenticated]