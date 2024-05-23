from django.db import models
from process.models import Process
from service.models import Service
from users.models import CustomUser

# Create your models here.

class ServiceProcess(models.Model):
    process_id = models.ForeignKey(Process, on_delete=models.CASCADE, blank=False,null=False)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE, null=False,blank=False)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False, null=False)
    