from django.contrib import admin
from .models import Car, CustomUser, SlotBooking
from django.contrib.auth.admin import UserAdmin


# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'seats', 'car_type']
    search_fields = ['name']
    list_filter = ['seats', 'car_type']


class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'email', 'username', 'first_name', 'last_name', 'address', 'created']
    search_fields = ['username']
    list_filter = ['username']


UserAdmin.fieldsets += (
    (
        'Custom fields', {
            'fields': ('address', 'created')
        }
    ),
)


class SlotBookingAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'car_name', 'duration', 'amount', 'booking_time']
    search_fields = ['customer_name']
    list_filter = ['customer_name', 'car_name', 'amount']


admin.site.register(Car, CarAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(SlotBooking, SlotBookingAdmin)
