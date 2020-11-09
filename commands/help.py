from telegram import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup


def help(update, context):
    help_text = (
        "I understand these commands: \n"
        "/help - List the commands that I understand \n"
        "/xkcd - Get an xkcd comic. Random if no argument given.\n"
        "/links - Get links to reach JODC.\n"
        "/meetup - Get next info about next meetup.\n\n"
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
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
        reply_markup=url_reply_markup
    )
