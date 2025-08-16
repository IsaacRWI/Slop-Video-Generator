import tweepy
from dotenv import load_dotenv
import os

load_dotenv()
auth = tweepy.OAuth1UserHandler(
    os.getenv("consumer_key"), os.getenv("consumer_secrets"), os.getenv("access_token"), os.getenv("access_token_secret")
)