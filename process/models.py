from django.db import models

# Create your models here.

class Process(models.Model):
    process_price = models.IntegerField(null=False, blank=False)
    process_name = models.CharField(max_length=64, blank=False, null=False)
    process_description = models.CharField(max_length=100, blank=False, null=False)
