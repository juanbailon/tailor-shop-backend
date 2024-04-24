from django.db import models

from users.models import CustomUser

# Create your models here.

class RawMaterial(models.Model):
    MATERIAL_TYPE = (
        ('Hilo', 'Hilo'), 
        ('Tela', 'Tela'),
        ('Cierre', 'Cierre'),
        ('Resorte', 'Resorte'),
        ('Aguja', 'Aguja'),
    )

    UNIT_OF_MEASURE = (
        ('Metros cuadrados', 'Metros cuadrados'), 
        ('Metros', 'Metros'),
        ('Unidad', 'Unidad'),
        ('Centimetros', 'Centimetros'),
    )
    user_register = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name="meterials_registered")
    name = models.CharField(max_length=100, null=False)
    material_type = models.CharField(choices = MATERIAL_TYPE, max_length = 30, null = False)
    remaining_amount = models.DecimalField(max_digits = 5, decimal_places = 2, null = False)
    unit_price = models.DecimalField(max_digits = 6, decimal_places = 2, null = False)
    unit_of_measure = models.CharField(choices = UNIT_OF_MEASURE, max_length = 30, null = False)

    class Meta:
        ordering = ["name"]