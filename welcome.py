from html import escape
import logging

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
