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
    user_register = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name="meterials_registered", blank=True)
    name = models.CharField(max_length=100, blank=True)
    material_type = models.CharField(choices=MATERIAL_TYPE, max_length=30, blank=True)
    remaining_amount = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    unit_of_measure = models.CharField(choices=UNIT_OF_MEASURE, max_length=30, blank=True)
    is_active = models.BooleanField(default=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name
