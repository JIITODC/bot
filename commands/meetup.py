import json
from html import escape
import logging
import os
import telegram
from telegram import Bot, user, ChatMember

root = logging.getLogger()
root.setLevel(logging.INFO)

logging.basicConfig(
    level=logging.INFO,
    format="""%(asctime)s - %(name)s - %(levelname)s
     - %(message)s""",
)
logger = logging.getLogger(__name__)
token = os.getenv("token")

with open("data_file.json", "r+") as read_file:
    data = json.load(read_file)

meetup_setters=['administrator','creator']
def meetup(update, context):
    chat_id = update.message.chat.id
    text=f"Next JODC Meetup:\nTitle: {data['Title']}\nDate: {data['Date']}\nTime: {data['Time']}\nPlatform: {data['Platform']}\nLink: {data['Link']}"
    context.bot.send_message(chat_id=chat_id, text=text)


def set_meetup(update, context):
    bot = Bot(token)
    chat_id = update.message.chat.id
    user_id = update.effective_user.id
    is_admin=bot.get_chat_member(user_id=user_id,chat_id=chat_id)
    if is_admin['status'] in meetup_setters:
        message=update.message.text.split(" - ")
        mess=update.message.text.partition(" ")[2]
        if not mess:
            text="To set meetup data use the following format:\n/set_meetup - title - date - time - platform - link "
            context.bot.send_message(chat_id=chat_id, text=text)
            return
        data['Title']=message[1]
        data['Date']= message[2]
        data['Time']= message[3]
        data['Platform']= message[4]
        data['Link']= message[5]
        with open("data_file.json", "w+") as write_file:
            json.dump(data, write_file)
        context.bot.send_message(chat_id=chat_id, text="Meetup added successfully!")
    else:
        context.bot.send_message(chat_id=chat_id, text="Sorry!\nOnly admins and creator can set meetup data")
