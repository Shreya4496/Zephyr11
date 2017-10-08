from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Location)
admin.site.register(FlightStatus)
admin.site.register(User)
admin.site.register(Flight)
admin.site.register(MyFlights)
admin.site.register(TUsers)
admin.site.register(ExistingOffers)
admin.site.register(PotentialOffers)
