from bot.bot import *

def select_language():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('English🇺🇸', callback_data='us'))
    markup.add(InlineKeyboardButton('Rusian🇷🇺', callback_data='ru'))
    return markup

