const { Telegraf } = require('telegraf')
const dotenv = require('dotenv')

dotenv.config()

const bot = new Telegraf(process.env.BOT_TOKEN)
const { onStart } = require('./commands/start')

onStart(bot)

bot.launch()
