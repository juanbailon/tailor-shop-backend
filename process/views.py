from rest_framework import generics, permissions, status

from process.models import Process
from raw_materials.serializers import RawMaterialSerializer
from .serializers import ProcessSerializer


class CreateProcessView(generics.CreateAPIView):
    serializer_class = ProcessSerializer
    permission_classes = [permissions.IsAuthenticated]


class ListProcessView(generics.ListAPIView):
    serializer_class = RawMaterialSerializer
    permission_classes = [permissions.IsAuthenticated]
    