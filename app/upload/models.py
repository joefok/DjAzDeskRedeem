from django.db import models


# Create your models here.
class Register(models.Model):
    token = models.CharField(max_length=255)
    assign_seat = models.CharField(max_length=5)
    pass
