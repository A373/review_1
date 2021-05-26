from django.db import models


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


class Customer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    phone = models.BigIntegerField()
    address = models.TextField()
    created = models.DateTimeField()

    def __str__(self):
        return str(self.id) + '-' + str(self.name)

    class Meta:
        verbose_name_plural = 'customers'


class SlotBooking(models.Model):
    customer_name = models.OneToOneField(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    car_name = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, blank=True)
    duration = models.IntegerField()
    amount = models.IntegerField()
    booking_time = models.DateTimeField()
