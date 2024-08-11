import json
import tweepy


def post_tweet(up: bool):
    with open('keys.json') as f:
        json_data = json.load(f)
    api_key = json_data.get("api_key")
    api_secret = json_data.get("api_secret")
    bearer_token = json_data.get("bearer_token")
    access_token = json_data.get("access_token")
    access_token_secret = json_data.get("access_token_secret")
    client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
    auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    if up:
        return client.create_tweet(text='eaula voltou :)')
    elif not up:
        return client.create_tweet(text='eaula caiu :(')
