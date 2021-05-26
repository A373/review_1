from django.contrib import admin
from .models import Car, Customer, SlotBooking


# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'seats', 'car_type']
    search_fields = ['name']
    list_filter = ['seats', 'car_type']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'address', 'created']
    search_fields = ['name']
    list_filter = ['name']


class SlotBookingAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'car_name', 'duration', 'amount', 'booking_time']
    search_fields = ['customer_name']
    list_filter = ['customer_name', 'car_name', 'amount']


admin.site.register(Car, CarAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(SlotBooking, SlotBookingAdmin)
