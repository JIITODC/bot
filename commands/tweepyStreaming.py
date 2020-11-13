import tweepy
import json
import os

# Using the twitter streaming api to get the latest tweets.

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


def tweets(update, context):
    class StdOutListener(tweepy.StreamListener):

        def on_data(self, data):
            data = json.loads(data)
            if 'delete' in data:
                return
            if data['user']['screen_name'] != 'jiitodc':
                return
            chat_id = update.message.chat.id
            text = f"https://twitter.com/jiitodc/status/{data['id_str']}"
            context.bot.send_message(chat_id=chat_id, text=text)
            return True

        def on_error(self, status):
            chat_id = update.message.chat.id
            text = "Something happened."
            context.bot.send_message(chat_id=chat_id, text=text)
            print(status)

    listener = StdOutListener()

    stream = tweepy.Stream(auth=api.auth, listener=listener)

    stream.filter(follow=[
        '1025405816839405569'], is_async=True)

# JODC twitter ID => '1025405816839405569'(It's public anyway)
