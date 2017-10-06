from django.shortcuts import render
from trend_promotion.models import *
from django.views.decorators.csrf import csrf_exempt
import smtplib
from django.core.mail import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
import requests
from django.http import JsonResponse


@csrf_exempt
def newUpdate(request):
    if request.method=='POST':
        fltno=request.POST.get('flightno')

        try:
            fltobj = FlightStatus.objects.get(flightno=fltno)
        except ObjectDoesNotExist:
            return JsonResponse("not exists",safe=False)

        #depart = request.POST.get('departure_time')
        #arriv = request.POST.get('arrival_time')
        gaten = request.POST.get('gateno')
        usern = request.POST.get('user_name')

        try:
            userobj= User.objects.get(user_name=usern)
        except ObjectDoesNotExist:
            return JsonResponse("not exists",safe=False)

        emailid=userobj.email
        #if depart:
         #   fltobj.departure_time=depart
        #if arriv:
         #   fltobj.arrival_time=arriv
        fltobj.gateno=gaten
        fltobj.save()
        """
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("", "zephyrvistara")
        msg = "Your latest details are: "+"departure time: "+""+" arrival time: "+""+" gate no: "+gaten
        server.sendmail("vistarabuddy96@gmail.com", emailid, msg)
        server.quit()
        """
        text = "Your latest boarding details for flight number: "
        text+=fltno
        #text += " are: \n departure time: "
        #text += fltobj.departure_time
        #text += " \narrival time: "
        #text +=fltobj.arrival_time
        text +=" \n gate no: "
        text += gaten
        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(text, 'plain')
        msg = MIMEMultipart('alternative')
        msg.attach(part1)
        subject = "VISTARA: Boarding update"
        msg = """\From: %s\nTo: %s\nSubject: %s\n\n%s""" % ("vistarabuddy96@gmail.com", emailid, subject, msg.as_string())
        # Use gmail's smtp server to send email. However, you need to turn on the setting "lesssecureapps" following this link:
        # https://www.google.com/settings/security/lesssecureapps
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login("vistarabuddy96@gmail.com", "zephyrvistara")
        server.sendmail("vistarabuddy96@gmail.com", [emailid], msg)
        server.quit()


        return JsonResponse("done",safe=False)