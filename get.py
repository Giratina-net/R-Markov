import tweepy
from os import getenv
import datetime

API_KEY=getenv("API_KEY")
API_SECRET_KEY=getenv("API_SECRET_KEY")
ACCESS_TOKEN=getenv("ACCESS_TOKEN")
ACCESS_SECRET_TOKEN=getenv("ACCESS_SECRET_TOKEN")
BEARER_TOKEN=getenv("BEARER_TOKEN")
USER_ID="1195260361156395008"

def run():
    dt = datetime.datetime.today()
    dt = datetime.datetime.now() 
    dt2 = dt + datetime.timedelta(days=-1)
    client = tweepy.Client(bearer_token    = BEARER_TOKEN,
                        consumer_key    = API_KEY,
                        consumer_secret = API_SECRET_KEY,
                        access_token    = ACCESS_TOKEN,
                        access_token_secret = API_SECRET_KEY,
                        )
    START=dt2
    END=dt
    tweets = client.get_users_tweets(id=USER_ID, max_results=100,start_time=START,end_time=END)
    for text in tweets.data:
        if not "http" in text.text:
            if not "RT" in text.text: 
                if not "@" in text.text: 
                    with open('data.txt', 'a', encoding='utf-8') as f:
                        print(text, file=f)


