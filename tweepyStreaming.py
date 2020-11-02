import tweepy
import json
import twitter_token

# Using the twitter streaming api to get the latest tweets.

auth = tweepy.OAuthHandler(twitter_token.CONSUMER_KEY,
                           twitter_token.CONSUMER_SECRET)
auth.set_access_token(twitter_token.ACCESS_TOKEN,
                      twitter_token.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


def tweets(update, context):
    class StdOutListener(tweepy.StreamListener):

        def on_data(self, data):
            data = json.loads(data)
            chat_id = update.message.chat.id
            text = f"https://twitter.com/jiitodc/status/{data['id_str']}"
            context.bot.send_message(chat_id=chat_id, text=text)
            return True

        def on_error(self, status):
            print(status)

    listener = StdOutListener()

    stream = tweepy.Stream(auth=api.auth, listener=listener)

    stream.filter(follow=['1306472885624635394', '1025405816839405569'])
