from django.db import models
from users.models import CustomUser
import datetime

# Create your models here.

class Service(models.Model):
    SERVICE_TYPE = (
        ('Confeccion', 'Confeccion'), 
        ('Reparacion', 'Reparacion'),
    )
    user_register = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False )
    creation_date = models.DateField(null=False, default= datetime.date.today)
    delivery_date = models.DateField(null=False)
    service_price = models.IntegerField(null=False, blank=False)
    client_name = models.CharField(null= False, blank=False, max_length=64)
    client_phone = models.CharField(null= False, blank=False, max_length=64)
    service_type = models.CharField(choices=SERVICE_TYPE, max_length=30, null=False)
    service_description = models.CharField(null=False, max_length= 100)
    is_active = models.BooleanField(default=True, blank=False)