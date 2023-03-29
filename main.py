import telebot

from telebot import types
from flask import Flask, request
from services.config import BOT_TOKEN, APP_URL
from services.sugar import get_answer, insert_answer
from services.messages import BOT_COMMANDS

WEBHOOK_URL = f"{APP_URL}/{BOT_TOKEN}"

bot = telebot.TeleBot(BOT_TOKEN)
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL)

app = Flask(__name__)

menu_markup = telebot.types.ReplyKeyboardMarkup(row_width=2)

start_btn = telebot.types.KeyboardButton('/start')
about_btn = telebot.types.KeyboardButton('/about')
insert_btn = telebot.types.KeyboardButton('/insert')
help_btn = telebot.types.KeyboardButton('/help')
ask_btn = telebot.types.KeyboardButton('/ask')
menu_markup.add(start_btn, ask_btn, about_btn, insert_btn, help_btn)


@app.route('/' + BOT_TOKEN, methods=['POST'])
def receive_message():
    update = telebot.types.Update.de_json(request.get_json(force=True))
    bot.process_new_updates([update])

    return 'ok', 200


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, BOT_COMMANDS['start'], reply_markup=menu_markup)


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, BOT_COMMANDS['help'])


@bot.message_handler(commands=['about'])
def about(message):
    bot.send_message(message.chat.id, BOT_COMMANDS['about'])


@bot.message_handler(commands=['insert'])
def insert(message):
    insert_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    cancel_button = types.KeyboardButton(BOT_COMMANDS['cancel'])
    insert_keyboard.add(cancel_button)
    sent_message = bot.send_message(chat_id=message.chat.id, text=BOT_COMMANDS['insert'], reply_markup=insert_keyboard)
    bot.register_next_step_handler(sent_message, handle_input_text)


def handle_input_text(message):
    if message.text == BOT_COMMANDS['cancel']:
        bot.send_message(chat_id=message.chat.id, text=BOT_COMMANDS["cancel_action"])
    else:
        answer = insert_answer(message.text)
        bot.send_message(chat_id=message.chat.id, text=answer, reply_markup=menu_markup)


@bot.message_handler(commands=['ask'])
def insert(message):
    ask_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    cancel_button = types.KeyboardButton(BOT_COMMANDS['cancel'])
    ask_keyboard.add(cancel_button)
    sent_message = bot.send_message(chat_id=message.chat.id, text=BOT_COMMANDS['ask'], reply_markup=ask_keyboard)
    bot.register_next_step_handler(sent_message, handle_ask_text)


def handle_ask_text(message):
    if message.text == BOT_COMMANDS['cancel']:
        bot.send_message(chat_id=message.chat.id, text=BOT_COMMANDS["cancel_action"], reply_markup=menu_markup)
    else:
        answer = get_answer(message.text)
        bot.send_message(chat_id=message.chat.id, text=answer, reply_markup=menu_markup)

# if __name__ == '__main__':
#     # bot.polling()
#     bot.remove_webhook()
#     bot.set_webhook(url=WEBHOOK_URL)
#     app.run(host='0.0.0.0', port=8080, debug=False, threaded=True)
