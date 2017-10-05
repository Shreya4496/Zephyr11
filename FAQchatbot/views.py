from django.shortcuts import render


from django.http import HttpResponse
from django.template import Context, loader


def ChatBot(request):

    return render(request, 'chatbot.html')


