from django.shortcuts import render

from trend_promotion.models import *
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render


from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from django.http import HttpResponse
from Zephyr.forms import UserForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist


from django.contrib.auth import update_session_auth_hash

def DashBoard(request):
    return render(request, 'dashboard.html')

def LOC(request):
    return render(request, 'LOCPage.html')


def Offers(request):
    return render(request, 'offers.html')

def ChatBot(request):
    return render(request, 'chatbot.html')

def trips_all(request):
    posts = MyFlights.objects.all()
    print (posts)
    return render(request, "list.html", {'posts': posts})

def Profile(request):
    return render(request, 'profile.html')

def Login(request):
    if request.method == "POST":
        user_name = request.POST['user_name']
        password = request.POST['password']
        user = authenticate(user_name=user_name, password=password)
        u= User.objects.all().order_by('?')[:5]

        context = {
            'u' : u
        }
        if user is not None:
            if user.is_active():
                login(request, user)
                return redirect('dashboard.html')
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
                return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')
   # return render(request, self.template_name, {'form': form})


#CHANGE PASSWORD
def privacy(request):
    if request.method=="POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  #so that user remains logged in even after password change
            return HttpResponseRedirect('/homepage/')
        return HttpResponseRedirect('/privacysettings/')
    else :
        form = PasswordChangeForm(user=request.user)
        context ={
        "form": form,
        }
        return render(request,'privacy_settings.html',context)



def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user_name = form.cleaned_data['user_name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        user.save()
        user = authenticate(user_name=user_name, password=password, email=email)
        if user is not None:
            user.is_active = False
            user.save()
            id = user.id
            email = user.email
            send_email(email, id)
                #return render(request, 'thankyou.html')
            #if user.is_active:
                #login(request, user)
            q=1
            return render(request,'dashboard.html')
            #return render(request,'chat/after_reg.html',{'q': q})

        return render(request,'login.html')


    context ={
        "form": form,
    }
    return render(request, 'registration_form.html', context)


def send_email(toaddr,id):
	text = "Hi!\nHere is the link to activate your account:\nhttp://shreya07.pythonanywhere.com/register_activate/activation/?id=%s" %(id)
	# Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(text, 'plain')
	msg = MIMEMultipart('alternative')
	msg.attach(part1)
	subject="Activate your account at Vistara"
	msg="""\From: %s\nTo: %s\nSubject: %s\n\n%s""" %("sealdeal16@gmail.com",toaddr,subject,msg.as_string())
	#Use gmail's smtp server to send email. However, you need to turn on the setting "lesssecureapps" following this link:
	#https://www.google.com/settings/security/lesssecureapps
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login("sealdeal16@gmail.com","tcsproject")
	server.sendmail("sealdeal16@gmail.com",[toaddr],msg)
	server.quit()

def activate(request):
	id=int(request.GET.get('id'))
	user = User.objects.get(id=id)
	user.is_active=True
	user.save()
	return render(request,'dashboard.html')

def Logout(request):
    logout(request)
  #  return render(request, "homepage.html")
    return HttpResponseRedirect('/homepage/')

def DashBoard(request):
    return render(request, 'dashboard.html')

def LOC(request):
    return render(request, 'LOCPage.html')


def Offers(request):
    return render(request, 'offers.html')


