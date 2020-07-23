const onContribute = bot => {
  bot.command('contribute', (ctx) => {
    ctx.telegram.sendMessage(ctx.chat.id, 'To contribute click below:',
      {
        reply_markup: {
          inline_keyboard: [[{ text: 'Github Link', url: 'https://github.com/JIITODC/bot' }]]
        }
      })
  })
}
module.exports = { onContribute }
