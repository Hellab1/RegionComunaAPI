from django.db import models

# Create your models here.
class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=64)

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=64)
    region = models.ForeignKey(Region, related_name='region', on_delete=models.CASCADE)
