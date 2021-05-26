from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Car(models.Model):
    CAR_TYPES = [
        ('Ac', 'Ac'),
        ('General', 'General'),
    ]
    name = models.CharField(max_length=255)
    seats = models.IntegerField()
    car_type = models.CharField(max_length=255, choices=CAR_TYPES)

    def __str__(self):
        return str(self.name) + '-' + str(self.seats) + '-' + str(self.car_type)

    class Meta:
        verbose_name_plural = 'cars'


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)


class SlotBooking(models.Model):
    customer_name = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    car_name = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, blank=True)
    duration = models.IntegerField()
    amount = models.IntegerField()
    booking_time = models.DateTimeField()
