import logging
from html import escape
import json


from telegram import ParseMode
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters

from config import bot_name, token

with open("data_file.json", "r+") as read_file:
    data = json.load(read_file)

root = logging.getLogger()
root.setLevel(logging.INFO)

logging.basicConfig(
    level=logging.INFO,
    format="""%(asctime)s - %(name)s - %(levelname)s
     - %(message)s""",
)

logger = logging.getLogger(__name__)


def welcome(update, context, new_member):
    # Greets a person who joins the chat

    message = update.message
    chat_id = message.chat.id
    logger.info(
        "%s joined to chat %d (%s)",
        escape(new_member.first_name),
        chat_id,
        escape(message.chat.title),
    )
    text = data[str(chat_id)]
    if text is None:
        text = "Hello $username! Welcome to $title"

    text = text.replace("$username", new_member.first_name)
    text = text.replace("$title", message.chat.title)
    context.bot.send_message(chat_id=chat_id, text=text, parse_mode=ParseMode.HTML)


def start(update, context):

    chat_id = update.message.chat.id

    text = (
        f"Hello {update.message.chat.title}! "
        "I am the official bot of JODC. I will now greet anyone who joins this chat with a "
        "nice message 😊 \nCheck the /help command for more info!"
    )
    context.bot.send_message(chat_id=chat_id, text=text)


def help(update, context):
    help_text = (
        "Welcomes everyone that enters a group chat that this bot is a "
        "part of. By default, only the person who invited the bot into "
        "the group is able to change settings.\nCommands:\n\n"
        "/welcome - Set welcome message\n"
        "& help messages\n\n"
        "You can use _$username_ and _$title_ as placeholders when setting"
        " messages. [HTML formatting]"
        "(https://core.telegram.org/bots/api#formatting-options) "
        "is also supported.\n"
    )

    chat_id = update.message.chat.id
    context.bot.send_message(
        chat_id=chat_id,
        text=help_text,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
    )


def set_welcome(update, context):

    chat_id = update.message.chat.id

    message = update.message.text.partition(" ")[2]

    if not message:
        context.bot.send_message(
            chat_id=chat_id,
            text="To set message, you can take following example:\n"
            "<code>/welcome Hello $username, welcome to "
            "$title!</code>",
            parse_mode=ParseMode.HTML,
        )
        return

    data[str(chat_id)] = message

    with open("data_file.json", "w+") as write_file:
        json.dump(data, write_file)

    context.bot.send_message(chat_id=chat_id, text="Got it!")


def lock(update, context):
    """ Locks the chat, so only the invitee can change settings """

    chat_id = update.message.chat.id

    context.bot.send_message(chat_id=chat_id, text="Got it!")


def check(update, context):
    if update.message.new_chat_members:
        for new_member in update.message.new_chat_members:
            if new_member.username == bot_name:
                return start(update, context)
            else:
                return welcome(update, context, new_member)


def main():
    updater = Updater(token, workers=10, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("welcome", set_welcome))
    dp.add_handler(MessageHandler(Filters.status_update, check))

    """updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://yourherokuappname.herokuapp.com/' + TOKEN)"""
    updater.start_polling(timeout=30, clean=True)

    updater.idle()


if __name__ == "__main__":
    main()
