from __future__ import unicode_literals
import sys
from imp import reload

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





"""
def new_func(request):
    CONSUMER_KEY = 'fX5oAGHDPAvu6MGdOJpBVMg6m'
    CONSUMER_SECRET = 'KxVWhnFOHBiaQUAOAHXBeTZOaeEk0H9eHCwCX55a4V6RNYrIbP'
    ACCESS_TOKEN = '784601048790999041-98R3Yb1F6A1dTpy1mngaqNUSesl7lIE'
    ACCESS_SECRET = 'DFD91l7l4MDuizDBR9ThmMRKQunyRaryNV0ibH9IkPbwF'

    requests.get("https://api.twitter.com/oauth/authenticate?oauth_token=784601048790999041-98R3Yb1F6A1dTpy1mngaqNUSesl7lIE")
   # oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    #auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    #auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

   # api = tweepy.API(auth)
    url="https://api.twitter.com/1.1/friends/list.json?cursor=-1&screen_name=diti2205&skip_status=true&include_user_entities=false"
    #data = urllib2.request.urlopen(url).read()

    #print(pw)
    r = requests.get(url)
    dataj = json.loads(r.text)
    data=str(dataj)
    #res = data['users'][0]['screen_name']
    #print data
   # print dict['users'][0]['screen_name']
    if 'errors' in data:
        #parsed_json = json.loads(data)
        return JsonResponse("yes",safe=False)

    return JsonResponse("done",safe=False)

def my_func(request):

    CONSUMER_KEY = 'fX5oAGHDPAvu6MGdOJpBVMg6m'
    CONSUMER_SECRET = 'KxVWhnFOHBiaQUAOAHXBeTZOaeEk0H9eHCwCX55a4V6RNYrIbP'
    ACCESS_KEY = '784601048790999041-98R3Yb1F6A1dTpy1mngaqNUSesl7lIE'
    ACCESS_SECRET = 'DFD91l7l4MDuizDBR9ThmMRKQunyRaryNV0ibH9IkPbwF'
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)


#        tweet = scrape_some_data()
    api.update_status(status='Sending my first tweet via tweepy! at '+str(datetime.datetime.now()))
    return JsonResponse("",safe=False)
 #       time.sleep(300)
# Create your views here.

def follower_retrieve(request):
    CONSUMER_KEY = 'fX5oAGHDPAvu6MGdOJpBVMg6m'
    CONSUMER_SECRET = 'KxVWhnFOHBiaQUAOAHXBeTZOaeEk0H9eHCwCX55a4V6RNYrIbP'
    ACCESS_TOKEN = '784601048790999041-98R3Yb1F6A1dTpy1mngaqNUSesl7lIE'
    ACCESS_SECRET = 'DFD91l7l4MDuizDBR9ThmMRKQunyRaryNV0ibH9IkPbwF'
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    #change to user entered twitter handle
    userList=[]
    #Shreya96Gupta
    for user in tweepy.Cursor(api.friends, screen_name="Shreya96Gupta").items():
        if (user.followers_count>10000):
            userList.append(user.screen_name)

    #userList2=userList
    #userList.clear()
    #impList=[]
    #for item in userList:
    #   if (item.followers_count)>10000:
    #      impList.append(item)

    return JsonResponse(userList,safe=False)
    #print(user.screen_name)


def getEvents(request):
    import requests

    for item in list:
        response = requests.get(
            "https://www.eventbriteapi.com/v3/events/search/",
            headers={
                "Authorization": "Bearer CEIOE6PUYBL5MI2BJCW4",
            }, params={"q": str(item), },
            verify=True,  # Verify SSL certificate
        )

        print response.json()['events'][0]['name']['text'], ", ", response.json()['events'][0]['start']['timezone']
        print
        print response.json()['events'][4]['name']['text'], ", ", response.json()['events'][0]['start']['timezone']
def abc(request):
    TWITTER_CONSUMER_KEY = 'fX5oAGHDPAvu6MGdOJpBVMg6m'
    TWITTER_CONSUMER_SECRET = 'KxVWhnFOHBiaQUAOAHXBeTZOaeEk0H9eHCwCX55a4V6RNYrIbP'
    TWITTER_ACCESS_TOKEN_KEY = '784601048790999041-98R3Yb1F6A1dTpy1mngaqNUSesl7lIE'
    TWITTER_ACCESS_TOKEN_SECRET = 'DFD91l7l4MDuizDBR9ThmMRKQunyRaryNV0ibH9IkPbwF'

    # This is the twitter user that we will be profiling using our news classifier.
    # TWITTER_USER = 'raulgarreta'
    TWITTER_USER = 'Shreya96Gupta'

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
        """
"""
        Return the bios of the people that a user follows

        api -- the tweetpy API object
        twitter_account -- the Twitter handle of the user
        max_users -- the maximum amount of users to return
        """
""""

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

        response = requests.get("https://www.eventbriteapi.com/v3/events/search/",
                                headers={"Authorization": "Bearer CEIOE6PUYBL5MI2BJCW4", }, params={"q": str(item), },
                                verify=True, )
        finalList.append(str(response.json()['events'][0]['name']['text'].encode('utf8'))+", "+str(response.json()['events'][0]['start']['timezone'].encode('utf8')))
        finalList.append(str(response.json()['events'][1]['name']['text'].encode('utf8'))+", "+str(response.json()['events'][1]['start']['timezone'].encode('utf8')))

    return JsonResponse(finalList,safe=False)
"""