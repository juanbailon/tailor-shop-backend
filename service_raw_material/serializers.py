from rest_framework import serializers
from .models import ServiceRawMaterial
from raw_materials.models import RawMaterial


class ServiceRawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRawMaterial
        fields = '__all__'
        
    def create(self, validated_data):
        raw_material = RawMaterial.objects.get(pk=validated_data["raw_material_id"])
        new_remaining_amount = raw_material.remaining_amount - validated_data["raw_material_amount"]
        raw_material.remaining_amount = new_remaining_amount
        service_raw_material = ServiceRawMaterial(**validated_data)
        service_raw_material.save()
        raw_material.save()
        return service_raw_material

    def is_valid(self, *, raise_exception=False):
        if 'raw_material_amount' in self.initial_data and 'raw_material_id' in self.initial_data:
            raw_material = RawMaterial.objects.get(pk=self.initial_data["raw_material_id"])
            
            if raw_material.remaining_amount-self.initial_data["raw_material_amount"] < 0:
                self._errors = {'raw_material_amount': 'It is not enough material to complete the service.'}
                if raise_exception:
                    raise serializers.ValidationError(self.errors)
                return False
        return super().is_valid(raise_exception=raise_exception)  