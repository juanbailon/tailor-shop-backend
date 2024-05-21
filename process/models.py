from django.db import models
from users.models import CustomUser

# Create your models here.

class Process(models.Model):
    process_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False,blank=False)
    process_price = models.IntegerField(null=False, blank=False)
    process_name = models.CharField(max_length=64, blank=False, null=False)
    process_description = models.CharField(max_length=100, blank=False, null=False)
