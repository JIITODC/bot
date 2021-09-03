from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def issues(update, context):
    chat_id = update.message.chat_id
    buttons = [
        [
            InlineKeyboardButton(
                text="Open Issues", url="https://github.com/JIITODC/bot/issues?q=is%3Aopen+is%3Aissue"
            ),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    # update.message.reply_text(reply_markup=reply_markup)
    context.bot.send_message(
        chat_id=chat_id, text="Find all the open issues here:", reply_markup=reply_markup
    )



