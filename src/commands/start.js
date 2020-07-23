const onStart = bot => {
  bot.start((ctx) => {
    ctx.telegram.sendMessage(ctx.chat.id, "Hello , I'm JODC Bot. To join our channels click below:",
      {
        reply_markup: {
          inline_keyboard: [[{ text: 'JODC', url: 'https://t.me/jiitodc' }, { text: 'JODC Offtopic', url: 'https://t.me/jiitodc_offtopic' }]]
        }
      })
  })
}
module.exports = { onStart }
