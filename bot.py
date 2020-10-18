import logging
import random
import requests
import os
from bs4 import BeautifulSoup
from html import escape

from telegram import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters

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


def welcome(update, context, new_member):
    # Greets a person who joins the chat
    message = update.message
    chat_id = message.chat.id
    if new_member.username is None:
        username = new_member.first_name
    else:
        username = new_member.username
    logger.info(
        "%s joined to chat %d (%s)",
        escape(username),
        chat_id,
        escape(message.chat.title),
    )

    text = (
        f"Hello @{username}! Welcome to the {message.chat.title} "
        "telegram group!\n"
        "Please introduce yourself."
    )

    context.bot.send_message(chat_id=chat_id, text=text)


def xkcd(update, context):
    message = update.message
    chat_id = message.chat.id
    msg_text = message.text

    split_msg = str.split(msg_text)
    args = split_msg.__len__()
    if args == 2:
        logger.info("%s requested an XKCD", escape(message.from_user.username))
        xkcd_num = split_msg[1]
        xkcd_url = "https://xkcd.com/" + str(xkcd_num)
        res = requests.get(xkcd_url)
        if res.status_code == 404:
            context.bot.send_message(
                chat_id=chat_id, text="Sorry, this xkcd comic does not exist yet."
            )
            return 1

        xkcd_soup = BeautifulSoup(res.text, "html.parser")
        comic_elem = xkcd_soup.select("#comic > img:nth-child(1)")
        comic_url = "https:" + comic_elem[0].get("src")

        context.bot.send_photo(chat_id=chat_id, photo=comic_url)

    else:
        logger.info("%s requested an XKCD", escape(message.from_user.username))

        random.seed()
        xkcd_num = random.randint(1, 2300)

        xkcd_url = "https://xkcd.com/" + str(xkcd_num)
        res = requests.get(xkcd_url)
        res.raise_for_status()

        xkcd_soup = BeautifulSoup(res.text, "html.parser")
        comic_elem = xkcd_soup.select("#comic > img:nth-child(1)")
        comic_url = "https:" + comic_elem[0].get("src")

        context.bot.send_photo(chat_id=chat_id, photo=comic_url)


def links(update, context):
    chat_id = update.message.chat_id
    buttons = [
        [InlineKeyboardButton(text="Website", url="https://jiitodc.netlify.app")],
        [InlineKeyboardButton(text="GitHub", url="https://github.com/JIITODC/")],
        [InlineKeyboardButton(text="Telegram", url="https://t.me/jiitodc")],
        [
            InlineKeyboardButton(text="Discord", url="https://discord.gg/eFrP5Z"),
            InlineKeyboardButton(text="Twitter", url="https://twitter.com/jiitodc"),
        ],
        [
            InlineKeyboardButton(
                text="LinkedIn", url="https://www.linkedin.com/company/jodc/"
            ),
            InlineKeyboardButton(
                text="Facebook", url="https://www.facebook.com/jiitodc/"
            ),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    # update.message.reply_text(reply_markup=reply_markup)
    context.bot.send_message(
        chat_id=chat_id, text="Find JODC on:", reply_markup=reply_markup
    )


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
        "/help - List the commands that I understand \n"
        "/xkcd - Get an xkcd comic. Random if no argument given.\n"
        "/links - Get links to reach JODC.\n\n"
        "Contributions from the community help me in learning more.\n"
        "Do checkout my repo once."
    )
    chat_id = update.message.chat.id
    bot_repo_button = [
        {InlineKeyboardButton("Visit JODC-bot repo", "https://github.com/JIITODC/bot")}
    ]
    url_reply_markup = InlineKeyboardMarkup(bot_repo_button)
    context.bot.send_message(
        chat_id=chat_id,
        text=help_text,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
        reply_markup=url_reply_markup
    )


def unknown(update, context):
    chat_id = update.message.chat.id

    text = "Sorry, I don't know that command"
    context.bot.send_message(chat_id=chat_id, text=text)


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

    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("xkcd", xkcd))
    dp.add_handler(CommandHandler("links", links))
    dp.add_handler(MessageHandler(Filters.status_update, check))
    dp.add_handler(MessageHandler(Filters.command, unknown))

    """updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://yourherokuappname.herokuapp.com/' + TOKEN)"""
    updater.start_polling(timeout=30, clean=True)

    updater.idle()


if __name__ == "__main__":
    main()
