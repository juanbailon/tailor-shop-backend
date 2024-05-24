from rest_framework import serializers
from .models import Process


class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = '__all__'
    
    def create(self, validated_data):
        process = Process(**validated_data)
        process.save()
        return process 