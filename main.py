import telebot

from values import *
from classes import Converter, APIException
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def start_help(message):
    c = 'Это бот конвертации валюты. Введите команду в формате:\n<имя валюты><в какую валюту перевести><количество валюты>\n Для просмотра доступных валют введите команду /values "'
    bot.reply_to(message, c)


@bot.message_handler(commands=['values'])
def currency_(message):
    c = 'Доступные валюты:'
    for i in currency.keys():
        c = '\n'.join((c, i,))

    bot.reply_to(message, c)


@bot.message_handler(content_types='text')
def convert(message):
    try:
        tex = message.text.lower()
        tex = tex.split(' ')
        if len(tex) != 3:
            raise APIException('Слишком много параметров')
        val1, val2, num = tex
        price=Converter.get_price(val1,val2,num)
    except APIException as e:
        bot.reply_to(message,f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message,f'Ошибка Сервера.\n{e}')
    else:
        text = f'Цена {num} {val1} в  {val2} = {price}'
        bot.send_message(message.chat.id, text)


bot.polling()
