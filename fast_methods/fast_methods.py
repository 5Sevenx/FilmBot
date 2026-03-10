import re


def MarkDown(text):
    escape_chars = r'_*\[\]()~`>#+-=|{}.!\\'
    return ''.join(f'\\{c}' if c in escape_chars else c for c in text)

def wich_lan(text):
    if re.search(r'[а-яА-ЯёЁ]', text):
        return 'ru'
    else:
        return 'us'

