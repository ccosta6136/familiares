from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.
class Familiares(models.Model):
    nombre = models.CharField(max_length=40)
    telefono = models.IntegerField()