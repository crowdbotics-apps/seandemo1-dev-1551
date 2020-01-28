from django.conf import settings
from django.db import models


class Tesla(models.Model):
    "Generated Model"
    price = models.BigIntegerField()
    availableDate = models.DateField(null=True, blank=True,)
    color = models.TextField(null=True, blank=True,)


# Create your models here.
