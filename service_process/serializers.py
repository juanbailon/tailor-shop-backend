from rest_framework import serializers
from .models import ServiceProcess


class ServiceProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProcess
        fields = '__all__'
        
    def create(self, validated_data):
        service_process = ServiceProcess(**validated_data)
        service_process.save()
        return service_process    