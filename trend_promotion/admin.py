from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Location)
admin.site.register(FlightStatus)
admin.site.register(User)
admin.site.register(Flight)
admin.site.register(Complaint)
admin.site.register(pref)
admin.site.register(MyFlights)