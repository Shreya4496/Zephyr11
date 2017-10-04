from django.shortcuts import render


from django.http import HttpResponse
from django.template import Context, loader

def DashBoard(request):
    return render(request, 'dashboard.html')

def LOC(request):
    return render(request, 'LOCPage.html')