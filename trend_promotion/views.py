#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from imp import reload
from django.core.exceptions import ObjectDoesNotExist

#reload(sys)
#sys.setdefaultencoding('utf8')
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
from .models import *
from django.core.mail import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

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


@csrf_exempt
def abc(request):
    TWITTER_CONSUMER_KEY = 'fX5oAGHDPAvu6MGdOJpBVMg6m'
    TWITTER_CONSUMER_SECRET = 'KxVWhnFOHBiaQUAOAHXBeTZOaeEk0H9eHCwCX55a4V6RNYrIbP'
    TWITTER_ACCESS_TOKEN_KEY = '784601048790999041-98R3Yb1F6A1dTpy1mngaqNUSesl7lIE'
    TWITTER_ACCESS_TOKEN_SECRET = 'DFD91l7l4MDuizDBR9ThmMRKQunyRaryNV0ibH9IkPbwF'

    # This is the twitter user that we will be profiling using our news classifier.
    # TWITTER_USER = 'raulgarreta'
    TWITTER_USER = 'diti2205'

    ### Get user data with Twitter API

    # tweepy is used to call the Twitter API from Python
    import tweepy
    import re

    # Authenticate to Twitter API
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN_KEY, TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    from random import shuffle

    def get_friends_descriptions(api, twitter_account, max_users=100):

        user_ids = api.friends_ids(twitter_account)
        shuffle(user_ids)

        following = []
        for start in xrange(0, min(max_users, len(user_ids)), 100):
            end = start + 100
            following.extend(api.lookup_users(user_ids[start:end]))

        descriptions = []
        for user in following:
            description = re.sub(r'(https?://\S+)', '', user.description)

            # Only descriptions with at least ten words.
            if len(re.split(r'[^0-9A-Za-z]+', description)) > 10:
                descriptions.append(description.strip('#').strip('@'))

        return descriptions

    # Get the descriptions of the people that twitter_user is following.
    descriptions = get_friends_descriptions(api, TWITTER_USER, max_users=300)

    # print descriptions


    def get_tweets(api, twitter_user, tweet_type='timeline', max_tweets=200, min_words=5):

        tweets = []

        full_tweets = []
        step = 200  # Maximum value is 200.
        for start in xrange(0, max_tweets, step):
            end = start + step

            # Maximum of `step` tweets, or the remaining to reach max_tweets.
            count = min(step, max_tweets - start)

            kwargs = {'count': count}
            if full_tweets:
                last_id = full_tweets[-1].id
                kwargs['max_id'] = last_id - 1

            if tweet_type == 'timeline':
                current = api.user_timeline(twitter_user, **kwargs)
            else:
                current = api.favorites(twitter_user, **kwargs)

            full_tweets.extend(current)

        for tweet in full_tweets:
            text = re.sub(r'(https?://\S+)', '', tweet.text)

            score = tweet.favorite_count + tweet.retweet_count
            if tweet.in_reply_to_status_id_str:
                score -= 15

            # Only tweets with at least five words.
            if len(re.split(r'[^0-9A-Za-z]+', text)) > min_words:
                tweets.append((text, score))

        return tweets

    tweets = []
    tweets.extend(get_tweets(api, TWITTER_USER, 'timeline', 1000))  # 400 = 2 requests (out of 15 in the window).
    tweets.extend(get_tweets(api, TWITTER_USER, 'favorites', 400))  # 1000 = 5 requests (out of 180 in the window).

    tweets = map(lambda t: t[0], sorted(tweets, key=lambda t: t[1], reverse=True))[:500]

    # print tweets
    str1 = ' '.join(descriptions)
    import textrazor
    textrazor.api_key = "ee7f8918c74568497dced941f1b49d107165eeeee194b7686b9ddadb"
    client = textrazor.TextRazor(extractors=["entities", "topics"])
    response = client.analyze(str1)
    labels = []
    for topic in response.topics():
        if topic.score > 0.7:
            # print topic.label
            labels.append(topic.label)

    import requests
    finalList=[]
    cnt=0
    for item in labels:
        cnt=cnt+1
        if cnt>6:
            break
        val=False
        val2=False

        response = requests.get("https://www.eventbriteapi.com/v3/events/search/",
                                headers={"Authorization": "Bearer CEIOE6PUYBL5MI2BJCW4", }, params={"q": str(item), },
                                verify=True, )
        loc=str(response.json()['events'][0]['start']['timezone'].encode('utf8'))
        try:
            obj=ExistingOffers.objects.get(city_arrival=loc)
        except ObjectDoesNotExist:
            val=True

            try:
                objnew=PotentialOffers.objects.get(city_arrival=loc)
            except ObjectDoesNotExist:
                val2=True
                objins=PotentialOffers()
                objins.departure_time = str(response.json()['events'][0]['start']['local'].encode('utf8'))
                objins.arrival_time = str(response.json()['events'][0]['start']['local'].encode('utf8'))
                objins.city_boarded = "New Delhi"
                objins.city_arrival = loc
                objins.counter=1
                objins.save()

            if val2==False:
                objnew.counter=objnew.counter+1


        if val==False:
            finalList.append(str(response.json()['events'][0]['name']['text'].encode('utf8'))+", "+str(response.json()['events'][0]['start']['timezone'].encode('utf8')))
            finalList.append(str(response.json()['events'][0]['start']['local'].encode('utf8')+"  "))

        loc = str(response.json()['events'][1]['start']['timezone'].encode('utf8'))
        try:
            obj = ExistingOffers.objects.get(city_arrival=loc)
        except ObjectDoesNotExist:
            val = True

            try:
                objnew = PotentialOffers.objects.get(city_arrival=loc)
            except ObjectDoesNotExist:
                val2 = True
                objins = PotentialOffers()
                objins.departure_time = str(response.json()['events'][1]['start']['local'].encode('utf8'))
                objins.arrival_time = str(response.json()['events'][1]['start']['local'].encode('utf8'))
                objins.city_boarded = "New Delhi"
                objins.city_arrival = loc
                objins.counter = 1
                objins.save()

            if val2 == False:
                objnew.counter = objnew.counter + 1

        if val == False:

            finalList.append(str(response.json()['events'][1]['name']['text'].encode('utf8'))+", "+str(response.json()['events'][1]['start']['timezone'].encode('utf8')))
            finalList.append(str(response.json()['events'][1]['start']['local'].encode('utf8') + "  "))









        #finalList.append(str(response.json()['events'][0]['name']['text'].encode('utf8'))+", "+str(response.json()['events'][0]['start']['timezone'].encode('utf8')))
        #finalList.append(str(response.json()['events'][1]['name']['text'].encode('utf8'))+", "+str(response.json()['events'][1]['start']['timezone'].encode('utf8')))

    #return JsonResponse(finalList,safe=False)
    return render(request, 'trends.html', {'finalList':finalList})

def potList(request):

    potList=[]

    obj=PotentialOffers.objects.all()

    for item in obj:
        mystr=str(item.departure_time)+" "+str(item.arrival_time)+" "+str(item.city_boarded)+" "+str(item.city_arrival)+" "+str(item.counter)+" "
        potList.append(mystr)

    return JsonResponse(potList,safe=False)
@csrf_exempt
def nonVUser(request):

     Tobj=TUsers.objects.all()

     for item in Tobj:
         ids=item.temail
         try:
            Vobj=User.objects.get(email=ids)
         except ObjectDoesNotExist:
            present=False

            text = "Hello from Vistara! We have some travel offers that might interest you :)\n "
            #text += fltno
            # text += " are: \n departure time: "
            # text += fltobj.departure_time
            # text += " \narrival time: "
            # text +=fltobj.arrival_time
            #text += " \n gate no: "
            #text += gaten
            # Record the MIME types of both parts - text/plain and text/html.


            TWITTER_CONSUMER_KEY = 'fX5oAGHDPAvu6MGdOJpBVMg6m'
            TWITTER_CONSUMER_SECRET = 'KxVWhnFOHBiaQUAOAHXBeTZOaeEk0H9eHCwCX55a4V6RNYrIbP'
            TWITTER_ACCESS_TOKEN_KEY = '784601048790999041-98R3Yb1F6A1dTpy1mngaqNUSesl7lIE'
            TWITTER_ACCESS_TOKEN_SECRET = 'DFD91l7l4MDuizDBR9ThmMRKQunyRaryNV0ibH9IkPbwF'

            # This is the twitter user that we will be profiling using our news classifier.
            # TWITTER_USER = 'raulgarreta'
            """name = request.POST.get('tname')
            try:
                userObj = User.objects.get(twitter_name=name)
            except ObjectDoesNotExist:
                return JsonResponse("none", safe=False)
            """
            TWITTER_USER = 'diti2205'

            ### Get user data with Twitter API

            # tweepy is used to call the Twitter API from Python
            import tweepy
            import re

            # Authenticate to Twitter API
            auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
            auth.set_access_token(TWITTER_ACCESS_TOKEN_KEY, TWITTER_ACCESS_TOKEN_SECRET)
            api = tweepy.API(auth)

            from random import shuffle

            def get_friends_descriptions(api, twitter_account, max_users=100):

                user_ids = api.friends_ids(twitter_account)
                shuffle(user_ids)

                following = []
                for start in xrange(0, min(max_users, len(user_ids)), 100):
                    end = start + 100
                    following.extend(api.lookup_users(user_ids[start:end]))

                descriptions = []
                for user in following:
                    description = re.sub(r'(https?://\S+)', '', user.description)

                    # Only descriptions with at least ten words.
                    if len(re.split(r'[^0-9A-Za-z]+', description)) > 10:
                        descriptions.append(description.strip('#').strip('@'))

                return descriptions

            # Get the descriptions of the people that twitter_user is following.
            descriptions = get_friends_descriptions(api, TWITTER_USER, max_users=300)

            # print descriptions


            def get_tweets(api, twitter_user, tweet_type='timeline', max_tweets=200, min_words=5):

                tweets = []

                full_tweets = []
                step = 200  # Maximum value is 200.
                for start in xrange(0, max_tweets, step):
                    end = start + step

                    # Maximum of `step` tweets, or the remaining to reach max_tweets.
                    count = min(step, max_tweets - start)

                    kwargs = {'count': count}
                    if full_tweets:
                        last_id = full_tweets[-1].id
                        kwargs['max_id'] = last_id - 1

                    if tweet_type == 'timeline':
                        current = api.user_timeline(twitter_user, **kwargs)
                    else:
                        current = api.favorites(twitter_user, **kwargs)

                    full_tweets.extend(current)

                for tweet in full_tweets:
                    text = re.sub(r'(https?://\S+)', '', tweet.text)

                    score = tweet.favorite_count + tweet.retweet_count
                    if tweet.in_reply_to_status_id_str:
                        score -= 15

                    # Only tweets with at least five words.
                    if len(re.split(r'[^0-9A-Za-z]+', text)) > min_words:
                        tweets.append((text, score))

                return tweets

            tweets = []
            tweets.extend(
                get_tweets(api, TWITTER_USER, 'timeline', 1000))  # 400 = 2 requests (out of 15 in the window).
            tweets.extend(
                get_tweets(api, TWITTER_USER, 'favorites', 400))  # 1000 = 5 requests (out of 180 in the window).

            tweets = map(lambda t: t[0], sorted(tweets, key=lambda t: t[1], reverse=True))[:500]

            # print tweets
            str1 = ' '.join(descriptions)
            import textrazor
            textrazor.api_key = "ee7f8918c74568497dced941f1b49d107165eeeee194b7686b9ddadb"
            client = textrazor.TextRazor(extractors=["entities", "topics"])
            response = client.analyze(str1)
            labels = []
            for topic in response.topics():
                if topic.score > 0.7:
                    # print topic.label
                    labels.append(topic.label)
                    #labels.append(topic.label)

            import requests
            finalList = []
            cnt = 0
            for item in labels:
                cnt = cnt + 1
                if cnt > 6:
                    break
                val = False
                val2 = False
                response = requests.get("https://www.eventbriteapi.com/v3/events/search/",
                                        headers={"Authorization": "Bearer CEIOE6PUYBL5MI2BJCW4", },
                                        params={"q": str(item), },
                                        verify=True, )
                s=(str(response.json()['events'][0]['name']['text'].encode('utf8'))+ str(
                    response.json()['events'][0]['start']['timezone'].encode('utf8')))
                s+=(str(response.json()['events'][0]['start']['local'].encode('utf8')))
                s+="\n"
                s+= (str(response.json()['events'][1]['name']['text'].encode('utf8'))+str(
                    response.json()['events'][1]['start']['timezone'].encode('utf8')))
                s += (str(response.json()['events'][1]['start']['local'].encode('utf8') ))
            text+=s
            #ids=str(item.temail)

            part1 = MIMEText(text, 'plain')
            msg = MIMEMultipart('alternative')
            msg.attach(part1)
            subject = "VISTARA: Boarding update"
            msg = """\From: %s\nTo: %s\nSubject: %s\n\n%s""" % (
                "vistarabuddy96@gmail.com", ids, subject, msg.as_string())
            # Use gmail's smtp server to send email. However, you need to turn on the setting "lesssecureapps" following this link:
            # https://www.google.com/settings/security/lesssecureapps
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login("vistarabuddy96@gmail.com", "zephyrvistara")
            server.sendmail("vistarabuddy96@gmail.com", ids, msg)
            server.quit()

     return JsonResponse("Mail is sent to the linked account",safe=False)
