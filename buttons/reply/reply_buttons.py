from bot.bot import *
def start_account(lan):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if lan == 'us':
        button = types.KeyboardButton('👤Open account')
        markup.add(button)
        return markup
    if lan == 'ru':
        button = types.KeyboardButton('👤Открыть акаунт')
        markup.add(button)
        return markup
