import telebot

from flask import Flask
from services.config import BOT_TOKEN
from services.sugar import get_answer

bot = telebot.TeleBot(BOT_TOKEN)

app = Flask(__name__)


@bot.message_handler(func=lambda message: True)
# @app.route('/' + BOT_TOKEN, methods=['GET', 'POST'])
def echo_message(message):
    answer = get_answer(message.text)
    bot.reply_to(message, answer)


if __name__ == '__main__':
    bot.polling()
    # app.run()
