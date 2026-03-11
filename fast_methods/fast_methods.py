import re
from bot.bot import *

def MarkDown(text):
    escape_chars = r'_*\[\]()~`>#+-=|{}.!\\'
    return ''.join(f'\\{c}' if c in escape_chars else c for c in text)

def wich_lan(text):
    if re.search(r'[а-яА-ЯёЁ]', text):
        return 'ru'
    else:
        return 'us'

def get_username(user_tg_id):
    user_name = bot.get_chat(user_tg_id).username
    if user_name:
        return "@"+user_name
    else:
        return None

