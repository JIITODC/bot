import logging
import os
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters

from commands.links import links
from commands.help import help
from commands.xkcd import xkcd
from commands.welcome import welcome
from commands.meetup import set_meetup, meetup

bot_name = os.getenv("bot_name")
token = os.getenv("token")

root = logging.getLogger()
root.setLevel(logging.INFO)

logging.basicConfig(
    level=logging.INFO,
    format="""%(asctime)s - %(name)s - %(levelname)s
     - %(message)s""",
)

logger = logging.getLogger(__name__)
def start(update, context):
    chat_id = update.message.chat.id

    text = (
        "Hello everyone!\n\n"
        "I am the JODC-bot.\n"
        "If you want to know about what I can do, use the /help command\n"
    )
    context.bot.send_message(chat_id=chat_id, text=text)


def unknown(update, context):
    chat_id = update.message.chat.id

    text = "Sorry, I don't know that command"
    context.bot.send_message(chat_id=chat_id, text=text)


def check(update, context):
    if update.message.new_chat_members:
        for new_member in update.message.new_chat_members:
            if new_member.username == bot_name:
                return start(update, context)
            else:
                return welcome(update, context, new_member)


def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("xkcd", xkcd))
    dp.add_handler(CommandHandler("links", links))
    dp.add_handler(CommandHandler("set_meetup", set_meetup))
    dp.add_handler(CommandHandler("meetup", meetup))
    dp.add_handler(MessageHandler(Filters.status_update, check))
    dp.add_handler(MessageHandler(Filters.command, unknown))


    updater.start_polling(timeout=30, clean=True)

    updater.idle()


if __name__ == "__main__":
    main()