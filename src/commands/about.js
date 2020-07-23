const onAbout = bot => {
  bot.command('about', (ctx) => {
    ctx.reply("<a href='https://github.com/JIITODC/JODC'>Github Profile</a>", {
      parse_mode: 'Html'
    })
  })
}
module.exports = { onAbout }
