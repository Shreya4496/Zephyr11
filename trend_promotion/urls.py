from .views import *
from django.conf.urls import url
from django.contrib import admin

# appname = 'trend_promotion'

urlpatterns = [
    url(r'^storeloc/$', store_location, name='store_loc'),
    ]