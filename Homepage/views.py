from django.shortcuts import render


from django.http import HttpResponse
from django.template import Context, loader

def HomePage(request):
    return render(request, 'MainHomePage.html')