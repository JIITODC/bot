from telegram import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
import os

bot_name = os.getenv("bot_name")
bot_name.replace("_","\\_")

def help(update, context):
    help_text = (
        "I understand these commands: \n"
        "/help@"+bot_name+" - List the commands that I understand \n" 
        "/xkcd@"+bot_name+" - Get an xkcd comic. Random if no argument given.\n" 
        "/links@"+bot_name+" - Get links to reach JODC.\n"
        "/meetup@"+bot_name+" - Get next info about next meetup.\n\n"
        "Contributions from the community helps me in learning more.\n"
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
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
        reply_markup=url_reply_markup
    )
