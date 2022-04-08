import tweepy
import json
import csv

from model import model
gpt3 = model()


class tweetGetter:
    def __init__(self): 
        key = open('api_key.txt','r')

        keys = key.readlines()

        API_KEY = keys[0].strip()
        API_SECRET = keys[1].strip()
        ACCESS_TOKEN = keys[2].strip()
        ACCESS_SECRET = keys[3].strip()

        auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self.api = tweepy.API(auth)


    def get_tweets(self, user, howmany):
        tweets = self.api.user_timeline(screen_name=user, count=howmany, include_rts = True)#max tweets is 200
        return tweets

    def print_tweets(tweets): 
        for tweet in tweets:
            print(tweet.text)

    def tweet_response_to_jsonfile(tweets):
        with open('tweet.json', 'w', encoding='utf-8') as f:
            json.dump(tweets[0]._json, f, ensure_ascii=False, indent=4)
