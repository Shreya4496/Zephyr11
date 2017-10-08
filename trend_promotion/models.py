from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    phone_number=models.CharField(max_length=50)
    twitter_name=models.CharField(max_length=50)
    current_city=models.CharField(max_length=50)
    loyality_pts=models.CharField(max_length=50)
    def __unicode__(self):
       return self.User

class Flight(models.Model):
    flightno= models.CharField(max_length=50)
    departure_time=models.DateTimeField(auto_now=False,auto_now_add=False)
    arrival_time=models.DateTimeField(auto_now=False,auto_now_add=False)
    city_boarded=models.CharField(max_length=50)
    city_arrival=models.CharField(max_length=50)
    gateno=models.CharField(max_length=50)

class MyFlights(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    linked_no = models.ForeignKey(Flight, on_delete=models.CASCADE, default=2)
    trip_date= models.DateTimeField(auto_now=False,auto_now_add=False)
    from_loc=models.CharField(max_length=100)
    to_loc=models.CharField(max_length=100)
    status=models.CharField(max_length=100)

class TUsers(models.Model):
    user_name = models.CharField(max_length=50)
    temail = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    twitter_name = models.CharField(max_length=50)
    current_city = models.CharField(max_length=50)
    def __unicode__(self):
       return self.user_name




class ExistingOffers(models.Model):
    flightno = models.CharField(max_length=50)
    departure_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    arrival_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    city_boarded = models.CharField(max_length=50)
    city_arrival = models.CharField(max_length=50)
    price=models.CharField(max_length=50)

class PotentialOffers(models.Model):
    departure_time = models.DateTimeField(max_length=50)
    arrival_time = models.DateTimeField(max_length=50 )
    city_boarded = models.CharField(max_length=50)
    city_arrival = models.CharField(max_length=50)
    counter = models.IntegerField()

class FlightStatus(models.Model):
        flightno = models.CharField(max_length=50)
        user_name = models.ForeignKey(User, on_delete=models.CASCADE)
        departure_time = models.DateTimeField(auto_now=False, auto_now_add=False)
        arrival_time = models.DateTimeField(auto_now=False, auto_now_add=False)
        city_boarded = models.CharField(max_length=50)
        city_departed = models.CharField(max_length=50)
        gateno = models.CharField(max_length=50)
        update = models.CharField(max_length=50)

class Location(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    linked_pnr = models.ForeignKey(FlightStatus, on_delete=models.CASCADE,default=2)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
