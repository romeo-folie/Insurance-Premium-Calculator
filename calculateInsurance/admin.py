from django.contrib import admin
from calculateInsurance.models import Car, Driver, Insurance

# Register your models here.

admin.site.register(Car)
admin.site.register(Driver)
admin.site.register(Insurance)
