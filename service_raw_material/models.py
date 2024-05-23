from django.db import models
from raw_materials.models import RawMaterial
from service.models import Service


class ServiceRawMaterial(models.Model):
    raw_material_id = models.ForeignKey(RawMaterial, on_delete=models.CASCADE,blank=False,null=False)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE, blank=False,null=False)
    raw_material_amount = models.DecimalField(max_digits=5, decimal_places=2, blank=True)