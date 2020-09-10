from colorfield.fields import ColorField
from django.db import models

TREATMENT_TYPE_CHOICES = (
    (1, "CRUDO"),
    (2, "PINTADO"),
    (3, "ANODIZADO")
    )

class Extruder(models.Model):
    extruder_name = models.CharField(max_length=200)

    def __str__(self):
        return self.extruder_name

class ProductSystem(models.Model):
    extruder = models.ForeignKey(Extruder, on_delete=models.CASCADE)
    system_name = models.CharField(max_length=200)

    def __str__(self):
        return self.system_name

class Profile(models.Model):
    system = models.ForeignKey(ProductSystem, on_delete=models.CASCADE)
    profile_code = models.CharField(max_length=20)
    profile_pic = models.ImageField(upload_to = 'aluminum/images/', 
                                    default = 'aluminum/images/no-img.jpg')
    profile_length = models.DecimalField(max_digits=3, decimal_places=2, default=6.06)
    profile_weight = models.DecimalField(max_digits=5, decimal_places=3, default=0.000)

    def __str__(self):
        return self.profile_code

#ColorField is a class of the package django-colorfield. See documentation for further details.
class Treatment(models.Model):
    treatment_type = models.IntegerField(choices=TREATMENT_TYPE_CHOICES, 
                                        default=TREATMENT_TYPE_CHOICES[0])
    color_name = models.CharField(max_length=200)
    preview = ColorField(default='#FF0000')

    def __str__(self):
        return self.color_name
    