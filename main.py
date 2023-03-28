import telebot

from flask import Flask, request
from services.config import BOT_TOKEN, APP_URL
from services.sugar import get_answer
from services.messages import BOT_COMMANDS

WEBHOOK_URL = f"{APP_URL}/{BOT_TOKEN}"

bot = telebot.TeleBot(BOT_TOKEN)
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL)

app = Flask(__name__)


@app.route('/' + BOT_TOKEN, methods=['POST'])
def receive_message():
    update = telebot.types.Update.de_json(request.get_json(force=True))
    if update.message:
        try:
            message = update.message
            answer = BOT_COMMANDS[message.text]
            bot.send_message(message.chat.id, answer)
        except KeyError:
            answer = get_answer(message.text)
            bot.reply_to(message, answer)

    return 'ok', 200


# if __name__ == '__main__':
#     # bot.polling()
#     bot.remove_webhook()
#     bot.set_webhook(url=WEBHOOK_URL)
#     app.run(host='0.0.0.0', port=8080, debug=False, threaded=True)
