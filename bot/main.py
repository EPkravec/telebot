from config import token
# Подключаем модуль случайных чисел
import random

import telebot
from telebot import types
from script import browser, link_food, link_tort, link_pirojennoe, link_morojennoe, link_salat

bot = telebot.TeleBot(token)
tort_link_f = link_tort(browser)
food_link_f = link_food(browser)
pirojennoe_link_f = link_pirojennoe(browser)
ice_cream_link_f = link_morojennoe(browser)
sala_link_f = link_salat(browser)


@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Меню вкусняшек', '']])
    bot.send_message(message.from_user.id, text='Выбери свою вкусняшку', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Меню вкусняшек":
        keyboard = types.InlineKeyboardMarkup()
        tort = types.InlineKeyboardButton(text='Тортики', callback_data='tort')
        piroj = types.InlineKeyboardButton(text='Пироженное', callback_data='pirojeno')
        ice_cream = types.InlineKeyboardButton(text='Мороженное', callback_data='ice_cream')
        oter = types.InlineKeyboardButton(text='Разное', callback_data='food')
        salat = types.InlineKeyboardButton(text='Салаты', callback_data='salat')

        keyboard.add(tort, piroj, ice_cream, salat, oter)
        bot.send_message(message.from_user.id, text='Выбери свою вкусняшку', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Привет еда")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "food":
        msg = random.choice(food_link_f)
        bot.send_message(call.message.chat.id, msg)
    if call.data == "tort":
        msg = random.choice(tort_link_f)
        bot.send_message(call.message.chat.id, msg)
    if call.data == "pirojeno":
        msg = random.choice(pirojennoe_link_f)
        bot.send_message(call.message.chat.id, msg)
    if call.data == "ice_cream":
        msg = random.choice(ice_cream_link_f)
        bot.send_message(call.message.chat.id, msg)
    if call.data == "salat":
        msg = random.choice(sala_link_f)
        bot.send_message(call.message.chat.id, msg)


bot.polling(none_stop=True)
