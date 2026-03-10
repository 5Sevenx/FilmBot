from DB.bd_commands import create_new_user, get_user
from buttons.inline.inline_buttons import *
from buttons.reply.reply_buttons import *
from fast_methods.fast_methods import wich_lan
from text.text import *


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Select preferred language", parse_mode="Markdown",reply_markup=select_language())

@bot.message_handler(content_types=['text'])
def bot_message(message):
    user_tg_id = message.from_user.id
    if get_user(user_tg_id) is None:
        if message.text == "👤Open account" or "👤Открыть акаунт":
            lan = wich_lan(message.text)

            if lan == "us":
                create_new_user(user_tg_id, 'us')
            else:
                create_new_user(user_tg_id, 'ru')

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    user_tg_id = call.from_user.id
    bot.delete_message(user_tg_id, call.message.message_id)
    if call.data == "us":
        bot.send_message(user_tg_id, ENG_START_TEXT, parse_mode="Markdown",reply_markup=start_account(call.data))
        return
    elif call.data == "ru":
        bot.send_message(user_tg_id, RUS_START_TEXT, parse_mode="Markdown",reply_markup=start_account(call.data))
        return

bot.polling(non_stop=True)