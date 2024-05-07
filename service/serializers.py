from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'
        extra_kwargs = {
            "user_register": {"required": True}
        }
    
    def create(self, validated_data):
        service = Service(**validated_data)
        service.save()
        return service
    
    def update(self, instance, validated_data):
        instance.client_name = validated_data.get('client_name', instance.client_name)
        instance.client_phone = validated_data.get('client_phone', instance.client_phone)
        instance.delivery_date = validated_data.get('delivery_date', instance.delivery_date)
        instance.service_price = validated_data.get('service_price', instance.service_price)
        instance.service_description = validated_data.get('service_description', instance.service_description)
        instance.save()
        return instance