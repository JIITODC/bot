const onHelp = bot => {
  bot.help((ctx) => {
    ctx.reply('This Bot can perform the following commands:\n /help - shows this message\n /about - Know more about JODC\n /contribute - To help me upgrade')
  })
}
module.exports = { onHelp }
