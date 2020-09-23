# bot
JIITODC's very own telegram bot!

### Setup Instructions:

###### Get a bot from BotFather to test your changes locally:
1. Ping [BotFather](https://t.me/botfather) on Telegram
2. Send `/start`
3. Send `/newbot` to create a new bot
4. You'll be prompted for a name and username for your bot, send them
* You'll get a bot API token similar to: `xxxxxxxxxx:xxx-xxxx_TE9i5t9Fm4Pf9lyopLvw7Gk4ag`

###### Installing python dependencies:
1. Install pip using your system's package manager:
Example for ubuntu
`sudo apt install python3-pip`
verify the installation by:
`pip3 --version`
2. Navigate to the project directory and install python dependencies using: 
`pip3 install -r requirements.txt`
3. In config.py set:
`bot_name` to your bot's name (the one you set with **BotFather**),
`token` to the token provided by **BotFather**,
4. Make a file `data_file.json` and write `{}` in it
5. Make the changes you want to
6. Run the bot with:
`python3 bot.py`

* Add the bot to a group and test your changes