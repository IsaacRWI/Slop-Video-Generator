import tweepy
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()
auth = tweepy.OAuth1UserHandler(
    os.getenv("consumer_key"), os.getenv("consumer_secret"), os.getenv("access_token"), os.getenv("access_token_secret")
)
api = tweepy.API(auth, wait_on_rate_limit=True)

query = "'Elon Musk' 'Announced' -filter:retweets AND -filter:replies AND -filter:links"
number = 2

def search():
    try:
        tweets = api.search_tweets(q=query, lang="en", count=number, tweet_mode = "extended")
        attribute_container = [[tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source, tweet.full_text] for tweet in tweets]
        columns = ["User", "Date Created", "Likes", "Source", "Content"]
        tweets_df = pd.DataFrame(attribute_container, columns=columns)
    except Exception as e:
        print(f"Status failed on {e}")
