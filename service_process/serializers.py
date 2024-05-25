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
    
class ServiceProcessInfoSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user_id.email', read_only=True)
    process_name = serializers.CharField(source = 'process_id.process_name', read_only=True)
    process_price = serializers.CharField(source = 'process_id.process_price', read_only=True)
    class Meta:
        model = ServiceProcess
        fields = [
            'user_id',
            'email',
            'process_id',
            'process_name',
            'process_price',
            'service_id'
        ]