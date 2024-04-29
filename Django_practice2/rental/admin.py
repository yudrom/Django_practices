from django.contrib import admin
from rental import models


admin.site.register(models.Car)
admin.site.register(models.RentalAgency)
