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

token = '5012000049:AAEMRbdVS66kUc3klMK8Olr1w_4UzSr5S9Q'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Подать заявку']])
    bot.send_message(message.from_user.id,
                     text='Добрый день\nВас приветствует бот для подачи заявок для заказа телеграмм бота\n',
                     reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global zayavka
    if message.text == "Подать заявку":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(
            *[types.KeyboardButton(name) for name in
              ['Чат бот - Автоворонка', 'Чат бот - Продажи', 'Чат бот - Другое']])
        keyboard.add(*[types.KeyboardButton(name) for name in ['Написать мне']])
        bot.send_message(message.from_user.id, text='Выбери что ты хочешь', reply_markup=keyboard)

    elif message.text == "Чат бот - Автоворонка":
        zayavka = message.text
        bot.send_message(message.from_user.id, 'Укажите тематику чат-бота')
        bot.register_next_step_handler(message, get_name_org)

    elif message.text == "Чат бот - Продажи":
        zayavka = message.text
        bot.send_message(message.from_user.id, 'Укажите тематику чат-бота')
        bot.register_next_step_handler(message, get_name_org)

    elif message.text == "Чат бот - Другое":
        zayavka = message.text
        bot.send_message(message.from_user.id, 'Укажите тематику чат-бота')
        bot.register_next_step_handler(message, get_name_org)
    elif message.text == "Написать мне":
        zayavka = message.text
        bot.send_message(message.from_user.id, 'https://t.me/Kravecegor')


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
        application = 'Python\n' + application
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
    bot.send_message(message.from_user.id, 'Дополнительные комментарии / ТЗ')
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
