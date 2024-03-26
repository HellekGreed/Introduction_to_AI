import telebot
from random import *
import json
import requests
import math

API_TOKEN='7034584440:AAGI7efk_V0Gfg10cMFzDBykdRe5l72rmXI'
bot = telebot.TeleBot(API_TOKEN)

API_URL='https://7012.deeppavlov.ai/model'


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Здравствуйте я помогу вам решить квадратные уровнения")
    bot.send_message(message.chat.id, "Введите коэффициенты для уравнения ax^2 + bx + c = 0 a b c через пробел")
    bot.send_message(message.chat.id, "Или можете ввести /wiki запрос что бы узнать интересные факты о запросе")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    dig = message.text.split()
    a = int(dig[0])
    b = int(dig[1])
    c = int(dig[2])
    discr = b**2 - 4 * a * c
    bot.send_message(message.chat.id, "Дискриминант D = %.0f" % discr)

    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        bot.send_message(message.chat.id, "x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif discr == 0:
        x = -b / (2 * a)
        bot.send_message(message.chat.id, "x = %.2f" % x)
    else:
        bot.send_message(message.chat.id, "Корней нет")

@bot.message_handler(commands=['wiki'])
def wiki(message):
    quest = message.text.split()[1:]
    qq=" ".join(quest)
    data = { 'question_raw': [qq]}
    try:
        res = requests.post(API_URL,json=data,verify=False).json()
        bot.send_message(message.chat.id, res)
    except:
        bot.send_message(message.chat.id, "Я не смог ничего найти.")

bot.polling()
