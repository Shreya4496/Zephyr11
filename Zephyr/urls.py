"""Zephyr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from Homepage.views import *
from Zephyr.views import *
from FAQchatbot.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^homepage/$', HomePage, name='homepage'),
url(r'^dashboard/$', DashBoard, name='homepage'),
url(r'^locpage/$', LOC, name='homepage'),
url(r'^trend_promotion/',include('trend_promotion.urls',namespace="trend_promotion")),
url(r'^chatbot/$', ChatBot, name='homepage'),
    url(r'^offers/$', Offers, name='offers'),
]
