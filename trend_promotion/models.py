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

class FlightStatus(models.Model):
    pnr= models.CharField(max_length=50)
    flight_username = models.ForeignKey(User, on_delete=models.CASCADE)
    departure_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    arrival_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    city_boarded=models.CharField(max_length=50)
    city_departed=models.CharField(max_length=50)
    gateno=models.CharField(max_length=50)
    update=models.CharField(max_length=50)

class Flight(models.Model):
    pnr= models.CharField(max_length=50)
    departure_time=models.DateTimeField(auto_now=False,auto_now_add=False)
    arrival_time=models.DateTimeField(auto_now=False,auto_now_add=False)
    city_boarded=models.CharField(max_length=50)
    city_arrival=models.CharField(max_length=50)
    gateno=models.CharField(max_length=50)
    update=models.CharField(max_length=50)

class Preferences(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    flight_pnr=models.ForeignKey(FlightStatus, on_delete=models.CASCADE)
    cat1=models.ForeignKey(User, on_delete=models.CASCADE)
    cat2=models.ForeignKey(User, on_delete=models.CASCADE)
    cat3=models.ForeignKey(User, on_delete=models.CASCADE)
    cat4=models.ForeignKey(User, on_delete=models.CASCADE)
    cat5=models.ForeignKey(User, on_delete=models.CASCADE)


class Complaint(models.Model):
    user_name=models.ForeignKey(User,on_delete=models.CASCADE)
    linked_pnr = models.ForeignKey(FlightStatus,on_delete=models.CASCADE)
    complaint_type = models.CharField(max_length=100)
    complaint_description = models.CharField(max_length=5000)

