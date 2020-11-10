import tweepy
import twitter_token

# Getting the latest tweet using /twitter command

auth = tweepy.OAuthHandler(twitter_token.CONSUMER_KEY,
                           twitter_token.CONSUMER_SECRET)
auth.set_access_token(twitter_token.ACCESS_TOKEN,
                      twitter_token.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


def twitter(update, context):
    user = api.get_user('jiitodc')
    print(user.status.id_str)
    chat_id = update.message.chat.id
    text = f"https://twitter.com/jiitodc/status/{user.status.id_str}"
    context.bot.send_message(chat_id=chat_id, text=text)
