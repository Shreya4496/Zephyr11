#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import requests
from rest_framework.response import Response
from django.http import JsonResponse
import json
#from urllib2 import urlopen
from twitter import Twitter,OAuth
import tweepy
import time
import datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt




# Create your views here.
def local_trends(request):
    TWITTER_CONSUMER_KEY = 'fX5oAGHDPAvu6MGdOJpBVMg6m'
    TWITTER_CONSUMER_SECRET = 'KxVWhnFOHBiaQUAOAHXBeTZOaeEk0H9eHCwCX55a4V6RNYrIbP'
    TWITTER_ACCESS_TOKEN_KEY = '784601048790999041-98R3Yb1F6A1dTpy1mngaqNUSesl7lIE'
    TWITTER_ACCESS_TOKEN_SECRET = 'DFD91l7l4MDuizDBR9ThmMRKQunyRaryNV0ibH9IkPbwF'

    # This is the twitter user that we will be profiling using our news classifier.
    #TWITTER_USER = 'raulgarreta'
    TWITTER_USER = 'GunjanS_96'
    import oauth2
    import json

    def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    	    consumer = oauth2.Consumer(key=TWITTER_CONSUMER_KEY, secret=TWITTER_CONSUMER_SECRET)
    	    token = oauth2.Token(key=TWITTER_ACCESS_TOKEN_KEY , secret=TWITTER_ACCESS_TOKEN_SECRET )
    	    client = oauth2.Client(consumer, token)
    	    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    	    loc= json.loads(content)
    	    city=[]
    	    #print loc
    	    #print loc[0]['name']
    	    cnt=10
    	    countr=[]
    	    for item in loc:
    	    	if(cnt<0):
    	    		break
    	    	cnt=cnt-1
    	    	#print item['name']
    	    	city.append(item['name'])
    	    	#print item['country']
    	    	countr.append(item['country'])


    	    #print(json.dumps(content, indent=2))
    	    print city
    	    print countr
    	    return city, countr

    city, countr = oauth_req( 'https://api.twitter.com/1.1/trends/available.json', 'abcdefg', 'hijklmnop' )
    promoevent=[]

    import requests
    for item in city:
    	response = requests.get("https://www.eventbriteapi.com/v3/events/search/",headers={"Authorization": "Bearer CEIOE6PUYBL5MI2BJCW4",}, params={"q": item },verify=True,)
    	#print response.json()['events'][0]['name']['text'] , " , location: " , item
    	#print
    	#print response.json()['events'][4]['name']['text'] , " , location: " , item
    	#print
        #promoevent.append(str(response.json()['events'][0]['name']['text'].encode('utf8')))
        #promoevent.append(str(response.json()['events'][1]['name']['text'].encode('utf8')))
        promoevent.append(str(response.json()['events'][0]['name']['text'].encode('utf8'))+str(response.json()['events'][0]['start']['timezone'].encode('utf8')))
        promoevent.append(str(response.json()['events'][0]['start']['local'].encode('utf8')))
        promoevent.append(str(response.json()['events'][1]['name']['text'].encode('utf8'))+str(response.json()['events'][1]['start']['timezone'].encode('utf8')))
        promoevent.append(str(response.json()['events'][1]['start']['local'].encode('utf8') ))

    
    #return JsonResponse(promoevent,safe=False)
    return render(request, 'local.html', {'promoevent':promoevent, 'city':city, 'countr':countr})
