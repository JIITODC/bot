import logging
from html import escape

from telegram import ParseMode
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters

from config import bot_name, token

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
        escape(new_member.username),
        chat_id,
        escape(message.chat.title),
    )
    text = (
        f"Hello @{new_member.username}! Welcome to the {message.chat.title} "
        "telegram group!\n"
        "Please introduce yourself."
    )
    context.bot.send_message(chat_id=chat_id, text=text)


def start(update, context):

    chat_id = update.message.chat.id

    text = (
        "Hello everyone!\n\n"
        "I am the JODC-bot.\n"
        "If you want to know about what I can do, use the /help command\n"
    )
    context.bot.send_message(chat_id=chat_id, text=text)


def help(update, context):
    help_text = (
        "I understand these commands: \n"
        "/help - List the commands that I understand \n\n"
        "Contributions from the JODC community helps me in learning more.\n"
        "https://github.com/JIITODC/bot"
    )
    chat_id = update.message.chat.id
    context.bot.send_message(
        chat_id=chat_id,
        text=help_text,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
    )


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
    dp.add_handler(MessageHandler(Filters.status_update, check))

    """updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://yourherokuappname.herokuapp.com/' + TOKEN)"""
    updater.start_polling(timeout=30, clean=True)

    updater.idle()


if __name__ == "__main__":
    main()
