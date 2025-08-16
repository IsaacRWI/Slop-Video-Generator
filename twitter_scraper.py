import tweepy
from dotenv import load_dotenv
import os

load_dotenv()
auth = tweepy.OAuth1UserHandler(
    os.getenv("consumer_key"), os.getenv("consumer_secret"), os.getenv("access_token"), os.getenv("access_token_secret")
)
api = tweepy.API(auth, wait_on_rate_limit=True)