import telebot

bot_token = '6281674243:AAGIVvqwlK-4SPyXjAGGc46ZWOlMAkpKpXQ'
bot = telebot.TeleBot(bot_token)


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


if __name__ == '__main__':
    bot.polling()
