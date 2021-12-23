#!/usr/bin/python3
# -*- coding: utf-8 -*-

import telebot
from telebot import types

name_org = ''
name_hum = ''
id_kiosk = ''
problem = ''
application = ''
zayavka = ''

token = '2122963915:AAEDJha3hGoamjvd6ATLkjMzz18K4wbDs_c'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Подать заявку']])
    bot.send_message(message.from_user.id, text='Добрый день\nВас приветствует бот Супер - сторисмейкера\n',
                     reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global zayavka
    if message.text == "Подать заявку":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(
            *[types.KeyboardButton(name) for name in ['Полное ведение аккаунта', 'Распаковка личности']])
        keyboard.add(
            *[types.KeyboardButton(name) for name in ['Анализ конкурентов', 'Анализ ЦА']])
        bot.send_message(message.from_user.id, text='Выбери что ты хочешь', reply_markup=keyboard)

    elif message.text == "Полное ведение аккаунта":
        zayavka = message.text
        bot.send_message(message.from_user.id, 'Укажитте ссылку на Ваш инстаграмм')
        bot.register_next_step_handler(message, get_name_org)

    elif message.text == "Распаковка личности":
        zayavka = message.text
        bot.send_message(message.from_user.id, 'Укажитте ссылку на Ваш инстаграмм')
        bot.register_next_step_handler(message, get_name_org)

    elif message.text == "Анализ конкурентов":
        zayavka = message.text
        bot.send_message(message.from_user.id, 'Укажитте ссылку на Ваш инстаграмм')
        bot.register_next_step_handler(message, get_name_org)

    elif message.text == "Анализ ЦА":
        zayavka = message.text
        bot.send_message(message.from_user.id, 'Укажитте ссылку на Ваш инстаграмм')
        bot.register_next_step_handler(message, get_name_org)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global application
    global name_org
    global name_hum
    global id_kiosk
    global problem
    global zayavka
    if call.data == "yes" or call.data == "Да, всё верно":
        bot.send_message(call.message.chat.id,
                         'Заявка отправлена, будет рассмотрена в ближайшее время. С вами свяжутся в течении 24 часов. Удачного дня!')
        bot.send_message(-1001672722503, text=application)
    elif call.data == "no" or call.data == "Нет, исправить":
        name_org = ''
        name_hum = ''
        id_kiosk = ''
        problem = ''
        application = ''
        zayavka = ''
        bot.send_message(call.message.chat.id, 'Выбери что ты хочешь')


def get_name_org(message):
    global name_org
    name_org = message.text
    bot.send_message(message.from_user.id, 'Введите Ваше Имя')
    bot.register_next_step_handler(message, get_name_hum)


def get_name_hum(message):
    global name_hum
    bot.send_message(message.from_user.id, 'Укажите, какой вид связи предпочтителен для дальнейшей проработки')
    name_hum = message.text
    bot.register_next_step_handler(message, get_kiosk)


def get_kiosk(message):
    global id_kiosk
    bot.send_message(message.from_user.id, 'Дополнительные комментарии')
    id_kiosk = message.text
    bot.register_next_step_handler(message, get_problem)


def get_problem(message):
    global problem
    global application
    global zayavka
    problem = message.text
    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да, всё верно', callback_data='yes')  # кнопка «Да»
    keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
    key_no = types.InlineKeyboardButton(text='Нет, исправить', callback_data='no')
    keyboard.add(key_no)
    application = f'Подана заявка - {zayavka}\nСсылка на инстаграмм: {name_org}\nЗаявка подана: {name_hum}\nВид связи {id_kiosk}\nДетали:{problem}'
    bot.send_message(message.from_user.id, text=application, reply_markup=keyboard)


bot.polling(none_stop=True)