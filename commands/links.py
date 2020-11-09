from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def links(update, context):
    chat_id = update.message.chat_id
    buttons = [
        [InlineKeyboardButton(text="Website", url="https://jiitodc.netlify.app")],
        [InlineKeyboardButton(text="GitHub", url="https://github.com/JIITODC/")],
        [InlineKeyboardButton(text="Telegram", url="https://t.me/jiitodc")],
        [
            InlineKeyboardButton(text="Discord", url="https://discord.gg/TC3DymJ"),
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
