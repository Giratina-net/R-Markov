import PrepareChain
import GenerateText
import tweepy
import re
import requests
from os import getenv

api_key=getenv("API_KEY")
api_secret_key=getenv("API_SECRET_KEY")
access_token=getenv("ACCESS_TOKEN")
access_secret_token=getenv("ACCESS_SECRET_TOKEN")
bearer_token=getenv("BEARER_TOKEN")

def run():
    f = open("data.txt",encoding="utf-8")
    text = f.read()
    f.close()
    chain = PrepareChain.PrepareChain(text)
    triplet_freqs = chain.make_triplet_freqs()
    chain.save(triplet_freqs, True)
    generator = GenerateText.GenerateText()
    client = tweepy.Client(consumer_key=api_key, consumer_secret=api_secret_key, bearer_token=bearer_token, access_token=access_token, access_token_secret=access_secret_token)
    auth = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_secret_key)
    auth.set_access_token(key=access_token, secret=access_secret_token)
    client.create_tweet(text=generator.generate())

if __name__ == '__main__':
    run()
print("start")
