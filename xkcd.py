import requests
from bs4 import BeautifulSoup
import logging
import random
from html import escape

root = logging.getLogger()
root.setLevel(logging.INFO)

logging.basicConfig(
    level=logging.INFO,
    format="""%(asctime)s - %(name)s - %(levelname)s
     - %(message)s""",
)

logger = logging.getLogger(__name__)


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