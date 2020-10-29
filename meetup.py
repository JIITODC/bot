import json
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

with open("data_file.json", "r+") as read_file:
    data = json.load(read_file)


def meetup(update, context):
    chat_id = update.message.chat.id
    text=f"Next JODC Meetup:\nTitle: {data['Title']}\nDate: {data['Date']}\nTime: {data['Time']}\nPlatform: {data['Platform']}\nLink: {data['Link']}"
    context.bot.send_message(chat_id=chat_id, text=text)


def set_meetup(update, context):
    chat_id = update.message.chat.id
    message=update.message.text.split(" - ")
    data['Title']=message[1]
    data['Date']= message[2]
    data['Time']= message[3]
    data['Platform']= message[4]
    data['Link']= message[5]
    with open("data_file.json", "w+") as write_file:
        json.dump(data, write_file)
    context.bot.send_message(chat_id=chat_id, text="Meetup added successfully!")