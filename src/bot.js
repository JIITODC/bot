const { Telegraf } = require('telegraf')
const dotenv = require('dotenv')

dotenv.config()

const bot = new Telegraf(process.env.BOT_TOKEN)
const { onStart } = require('./commands/start')
const { onHelp } = require('./commands/help')
const { onAbout } = require('./commands/about')
const { onContribute } = require('./commands/contribute')

onStart(bot)
onHelp(bot)
onAbout(bot)
onContribute(bot)

bot.launch()
