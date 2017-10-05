from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Location
# Create your views here.

@csrf_exempt
def store_location(request):
    print('yoyoyo')
    if request.method == 'POST' and request.is_ajax():
        print('in request method')
        print(request.POST)
        if 'lat' in request.POST:
            lat,long = request.POST['lat'],request.POST['long']
            print(lat)
            print(long)
            loc_obj = Location(lat=lat, long=long)
            loc_obj.save()
        else:
            print('nope')
    return render(request,'LOCPage.html')