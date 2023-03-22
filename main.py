import telebot

from services.config import BOT_TOKEN
from services.sugar import get_answer

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    answer = get_answer(message.text)
    bot.reply_to(message, answer)


if __name__ == '__main__':
    bot.polling()
