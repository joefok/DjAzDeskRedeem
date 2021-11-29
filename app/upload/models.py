from django.db import models


# Create your models here.
class RegisterSeat(models.Model):
    token = models.CharField(max_length=255)
    assign_seat = models.CharField(max_length=5)

    def __str__(self):
        return self.token
