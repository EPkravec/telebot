from setting import token

import random
import telebot
from telebot import types
from parsing import browser
from parsing import link_sladost, data_link_client

url = 'https://www.youtube.com/channel/UC16_fT1sHaIFNhnLg3kw1Jw'
bot = telebot.TeleBot(token)

# def connect_parse(links_foood):
#     for z in links_foood:
#         for i in links_foood[z].keys():
#             k = links_foood[z][i]
#             link_sladost(browser, i, k)
#     return i, k
#

dec_tort_links = link_sladost(browser, 'dec_tort',
                              'https://www.youtube.com/results?search_query=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82%D1'
                              '%8B+%D1%82%D0%BE%D1%80%D1%82%D0%BE%D0%B2+')
dec_pechenie_links = link_sladost(browser, 'dec_pechenie',
                                  'https://www.youtube.com/results?search_query=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82'
                                  '%D1%8B+%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D1%8C%D0%B5+')
dec_pirogi_links = link_sladost(browser, 'dec_pirogi',
                                'https://www.youtube.com/results?search_query=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82%D1'
                                '%8B+%D1%81%D0%BB%D0%B0%D0%B4%D0%BA%D0%B8%D0%B5+%D0%BF%D0%B8%D1%80%D0%BE%D0%B3%D0%B8')
dec_konfetu_links = link_sladost(browser, 'dec_konfetu',
                                 'https://www.youtube.com/results?search_query=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82'
                                 '%D1%8B+%D0%BA%D0%BE%D0%BD%D1%84%D0%B5%D1%82+')
dec_cheezkeik_links = link_sladost(browser, 'dec_cheezkeik',
                                   'https://www.youtube.com/results?search_query=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82'
                                   '%D1%8B+%D1%87%D0%B8%D0%B7%D0%BA%D0%B5%D0%B9%D0%BA%D0%BE%D0%B2')
dec_vostok_sladosti_links = link_sladost(browser, 'dec_vostok_sladosti',
                                         'https://www.youtube.com/results?search_query=%D1%80%D0%B5%D1%86%D0%B5%D0%BF'
                                         '%D1%82%D1%8B+%D0%B2%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D1%8B%D0%B5+%D1%81'
                                         '%D0%BB%D0%B0%D0%B4%D0%BE%D1%81%D1%82%D0%B8')
fruct_dec_multi_vce_links = link_sladost(browser, 'fruct_dec_multi_vce',
                                         'https://www.youtube.com/results?search_query=%D1%80%D0%B5%D1%86%D0%B5%D0%BF'
                                         '%D1%82%D1%8B+%D1%84%D1%80%D1%83%D0%BA%D1%82%D0%BE%D0%B2%D1%8B%D1%85+%D0%B4'
                                         '%D0%B5%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B2')
fruct_dec_yabloko_links = link_sladost(browser, 'fruct_dec_yabloko',
                                       'https://www.youtube.com/results?search_query=%D1%80%D0%B5%D1%86%D0%B5%D0%BF'
                                       '%D1%82%D1%8B+%D0%B4%D0%B5%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B2+%D0%B8%D0%B7'
                                       '+%D1%8F%D0%B1%D0%BB%D0%BE%D0%BA')
fruct_dec_malina_links = link_sladost(browser, 'fruct_dec_malina',
                                      'https://www.youtube.com/results?search_query=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1'
                                      '%82%D1%8B+%D0%B4%D0%B5%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B2+%D0%B8%D0%B7+%D0%BC'
                                      '%D0%B0%D0%BB%D0%B8%D0%BD%D1%8B')
fruct_dec_clubnika_links = link_sladost(browser, 'fruct_dec_clubnika',
                                        'https://www.youtube.com/results?search_query=%D1%80%D0%B5%D1%86%D0%B5%D0%BF'
                                        '%D1%82%D1%8B+%D0%B4%D0%B5%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B2+%D0%B8%D0%B7'
                                        '+%D0%BA%D0%BB%D1%83%D0%B1%D0%BD%D0%B8%D0%BA%D0%B8')
fruct_dec_gruwa_links = link_sladost(browser, 'fruct_dec_gruwa',
                                     'https://www.youtube.com/results?search_query=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1'
                                     '%82%D1%8B+%D0%B4%D0%B5%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B2+%D0%B8%D0%B7+%D0%B3'
                                     '%D1%80%D1%83%D1%88%D0%B8')
fruct_dec_banan_links = link_sladost(browser, 'fruct_dec_banan',
                                     'https://www.youtube.com/results?search_query=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1'
                                     '%82%D1%8B+%D0%B4%D0%B5%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B2+%D0%B8%D0%B7+%D0%B1'
                                     '%D0%B0%D0%BD%D0%B0%D0%BD%D0%B0')
fruct_dec_chenosliv_links = link_sladost(browser, 'fruct_dec_chenosliv',
                                         'https://www.youtube.com/results?search_query=%D1%80%D0%B5%D1%86%D0%B5%D0%BF'
                                         '%D1%82%D1%8B+%D0%B4%D0%B5%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B2+%D0%B8%D0%B7'
                                         '+%D1%87%D0%B5%D1%80%D0%BD%D0%BE%D1%81%D0%BB%D0%B8%D0%B2%D0%B0')
fruct_dec_smorodina_links = link_sladost(browser, 'fruct_dec_smorodina',
                                         'https://www.youtube.com/results?search_query=%D1%80%D0%B5%D1%86%D0%B5%D0%BF'
                                         '%D1%82%D1%8B+%D0%B4%D0%B5%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B2+%D0%B8%D0%B7'
                                         '+%D1%81%D0%BC%D0%BE%D1%80%D0%BE%D0%B4%D0%B8%D0%BD%D0%B0')
vup_ponchiki_links = link_sladost(browser, 'vup_ponchiki',
                                  'https://www.youtube.com/results?search_query=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82'
                                  '%D1%8B+%D0%B2%D1%8B%D0%BF%D0%B5%D1%87%D0%BA%D0%B0+%D0%BF%D0%BE%D0%BD%D1%87%D0%B8'
                                  '%D0%BA%D0%B8')
vup_maffin_links = link_sladost(browser, 'vup_maffin',
                                'https://www.youtube.com/results?search_query=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82%D1'
                                '%8B+%D0%B2%D1%8B%D0%BF%D0%B5%D1%87%D0%BA%D0%B0+%D0%BC%D0%B0%D1%84%D1%84%D0%B8%D0%BD'
                                '%D1%8B')
vup_kiksu_links = link_sladost(browser, 'vup_kiksu',
                               'https://www.youtube.com/results?search_query=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82%D1'
                               '%8B+%D0%B2%D1%8B%D0%BF%D0%B5%D1%87%D0%BA%D0%B0+%D0%BA%D0%B5%D0%BA%D1%81%D1%8B')
vup_slouki_links = link_sladost(browser, 'vup_slouki',
                                'https://www.youtube.com/results?search_query=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82%D1'
                                '%8B+%D0%B2%D1%8B%D0%BF%D0%B5%D1%87%D0%BA%D0%B0+%D1%81%D0%BB%D0%BE%D0%B9%D0%BA%D0%B8')
vup_sochniki_links = link_sladost(browser, 'vup_sochniki',
                                  'https://www.youtube.com/results?search_query=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82'
                                  '%D1%8B+%D0%B2%D1%8B%D0%BF%D0%B5%D1%87%D0%BA%D0%B0+%D1%81%D0%BE%D1%87%D0%BD%D0%B8'
                                  '%D0%BA%D0%B8')
vup_kylichi_links = link_sladost(browser, 'vup_kylichi',
                                 'https://www.youtube.com/results?search_query=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82'
                                 '%D1%8B+%D0%B2%D1%8B%D0%BF%D0%B5%D1%87%D0%BA%D0%B0+%D0%BA%D1%83%D0%BB%D0%B8%D1%87%D0'
                                 '%B8')
vup_plywki_links = link_sladost(browser, 'vup_plywki',
                                'https://www.youtube.com/results?search_query=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82%D1'
                                '%8B+%D0%B2%D1%8B%D0%BF%D0%B5%D1%87%D0%BA%D0%B0+%D0%BF%D0%BB%D1%8E%D1%88%D0%BA%D0%B8')
vup_blinchki_links = link_sladost(browser, 'vup_blinchki',
                                  'https://www.youtube.com/results?search_query=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82'
                                  '%D1%8B+%D0%B2%D1%8B%D0%BF%D0%B5%D1%87%D0%BA%D0%B0+%D0%B1%D0%BB%D0%B8%D0%BD%D1%87'
                                  '%D0%B8%D0%BA%D0%B8')
salat_ovowi_links = link_sladost(browser, 'salat_ovowi',
                                 'https://www.youtube.com/results?search_query=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82'
                                 '%D1%8B+%D0%BE%D0%B2%D0%BE%D1%89%D0%BD%D1%8B%D1%85+%D1%81%D0%B0%D0%BB%D0%B0%D1%82%D0'
                                 '%BE%D0%B2')
salat_myasnoi_links = link_sladost(browser, 'salat_myasnoi',
                                   'https://www.youtube.com/results?search_query=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82'
                                   '%D1%8B+%D0%BC%D1%8F%D1%81%D0%BD%D1%8B%D1%85+%D1%81%D0%B0%D0%BB%D0%B0%D1%82%D0%BE'
                                   '%D0%B2')
salat_rubnui_links = link_sladost(browser, 'salat_rubnui',
                                  'https://www.youtube.com/results?search_query=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82'
                                  '%D1%8B+%D1%80%D1%8B%D0%B1%D0%BD%D1%8B%D1%85+%D1%81%D0%B0%D0%BB%D0%B0%D1%82%D0%BE'
                                  '%D0%B2')
salat_smewanui_links = link_sladost(browser, 'salat_smewanui',
                                    'https://www.youtube.com/results?search_query=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1'
                                    '%82%D1%8B+%D1%81%D0%BC%D0%B5%D1%88%D0%B0%D0%BD%D0%BD%D1%8B%D1%85+%D1%81%D0%B0%D0'
                                    '%BB%D0%B0%D1%82%D0%BE%D0%B2')

if url:
    link_client, name_autor = data_link_client(browser, url)


@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if url:
        keyboard.add(*[types.KeyboardButton(name) for name in ['Лучшие рецепты от проффи %s' % name_autor]])
    keyboard.add(*[types.KeyboardButton(name) for name in ['Меню вкусняшек', '']])
    bot.send_message(message.from_user.id, text='Выбери свою вкусняшку', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Меню вкусняшек":
        keyboard = types.InlineKeyboardMarkup()
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        if url:
            keyboard.add(*[types.KeyboardButton(name) for name in ['Лучшие рецепты от проффи %s' % name_autor]])
        keyboard.add(*[types.KeyboardButton(name) for name in ['Десерты', 'Фруктовые десерты']])
        keyboard.add(*[types.KeyboardButton(name) for name in ['Выпечка', 'Салатики']])
        bot.send_message(message.from_user.id, text='Выбери свою вкусняшку', reply_markup=keyboard)
    elif message.text == "Десерты":
        keyboard = types.InlineKeyboardMarkup()
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        if url:
            keyboard.add(*[types.KeyboardButton(name) for name in ['Лучшие рецепты от проффи %s' % name_autor]])
        keyboard.add(*[types.KeyboardButton(name) for name in ['Тортики', 'Печенье', 'Пироги']])
        keyboard.add(*[types.KeyboardButton(name) for name in ['Конфеты', 'Чизкейки', 'Сладости востока', 'вернуться']])
        bot.send_message(message.from_user.id, text='Выбери свой десерт', reply_markup=keyboard)
    elif message.text == "Фруктовые десерты":
        keyboard = types.InlineKeyboardMarkup()
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        if url:
            keyboard.add(*[types.KeyboardButton(name) for name in ['Лучшие рецепты от проффи %s' % name_autor]])
        keyboard.add(*[types.KeyboardButton(name) for name in ['МультиВСЕ', 'Яблоко', 'Малина']])
        keyboard.add(*[types.KeyboardButton(name) for name in ['Клубника', 'Груша', 'Банан']])
        keyboard.add(*[types.KeyboardButton(name) for name in ['Чернослив', 'Смородина', 'вернуться']])
        bot.send_message(message.from_user.id, text='Выбери свой фруктовый десерт', reply_markup=keyboard)
    elif message.text == "Выпечка":
        keyboard = types.InlineKeyboardMarkup()
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        if url:
            keyboard.add(*[types.KeyboardButton(name) for name in ['Лучшие рецепты от проффи %s' % name_autor]])
        keyboard.add(*[types.KeyboardButton(name) for name in ['Пончики', 'Маффины', 'Кексы']])
        keyboard.add(*[types.KeyboardButton(name) for name in ['Слойки', 'Сочкники', 'Куличи']])
        keyboard.add(*[types.KeyboardButton(name) for name in ['Плюшки', 'Блинчики', 'вернуться']])
        bot.send_message(message.from_user.id, text='Выбери свою выпечку', reply_markup=keyboard)
    elif message.text == "Салатики":
        keyboard = types.InlineKeyboardMarkup()
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        if url:
            keyboard.add(*[types.KeyboardButton(name) for name in ['Лучшие рецепты от проффи %s' % name_autor]])
        keyboard.add(*[types.KeyboardButton(name) for name in ['Овощной', 'Мясной', 'Рыбный']])
        keyboard.add(*[types.KeyboardButton(name) for name in ['Смешаный', 'вернуться']])
        bot.send_message(message.from_user.id, text='Выбери свой салатик', reply_markup=keyboard)
    elif message.text == "вернуться":
        keyboard = types.InlineKeyboardMarkup()
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        if url:
            keyboard.add(*[types.KeyboardButton(name) for name in ['Лучшие рецепты от проффи %s' % name_autor]])
        keyboard.add(*[types.KeyboardButton(name) for name in ['Десерты', 'Фруктовые десерты']], )
        keyboard.add(*[types.KeyboardButton(name) for name in ['Выпечка', 'Салатики']])
        bot.send_message(message.from_user.id, text='Выбери свою вкусняшку', reply_markup=keyboard)
    elif (message.text == "Лучшие рецепты от проффи %s" % name_autor) and url:
        msg = random.choice(data_link_client)
        bot.send_message(message.chat.id, msg)
    elif message.text == "Тортики":
        msg = random.choice(dec_tort_links)
        bot.send_message(message.chat.id, msg)
    elif message.text == 'Печенье':
        msg = random.choice(dec_pechenie_links)
        bot.send_message(message.chat.id, msg)
    elif message.text == 'Пироги':
        msg = random.choice(dec_pirogi_links)
        bot.send_message(message.chat.id, msg)
    elif message.text == 'Конфеты':
        msg = random.choice(dec_konfetu_links)
        bot.send_message(message.chat.id, msg)
    elif message.text == 'Чизкейки':
        msg = random.choice(dec_cheezkeik_links)
        bot.send_message(message.chat.id, msg)
    elif message.text == 'Сладости востока':
        msg = random.choice(dec_vostok_sladosti_links)
        bot.send_message(message.chat.id, msg)
    elif message.text == 'МультиВСЕ':
        msg = random.choice(fruct_dec_multi_vce_links)
        bot.send_message(message.chat.id, msg)
    elif message.text == 'Яблоко':
        msg = random.choice(fruct_dec_yabloko_links)
        bot.send_message(message.chat.id, msg)
    elif message.text == 'Малина':
        msg = random.choice(fruct_dec_malina_links)
        bot.send_message(message.chat.id, msg)
    elif message.text == 'Клубника':
        msg = random.choice(fruct_dec_clubnika_links)
        bot.send_message(message.chat.id, msg)
    elif message.text == 'Груша':
        msg = random.choice(fruct_dec_gruwa_links)
        bot.send_message(message.chat.id, msg)
    elif message.text == 'Банан':
        msg = random.choice(fruct_dec_banan_links)
        bot.send_message(message.chat.id, msg)
    elif message.text == 'Чернослив':
        msg = random.choice(fruct_dec_chenosliv_links)
        bot.send_message(message.chat.id, msg)
    elif message.text == 'Смородина':
        msg = random.choice(fruct_dec_smorodina_links)
        bot.send_message(message.chat.id, msg)

    elif message.text == 'Пончики':
        msg = random.choice(vup_ponchiki_links)
        bot.send_message(message.chat.id, msg)
    elif message.text == 'Маффины':
        msg = random.choice(vup_maffin_links)
        bot.send_message(message.chat.id, msg)
    elif message.text == 'Кексы':
        msg = random.choice(vup_kiksu_links)
        bot.send_message(message.chat.id, msg)
    elif message.text == 'Слойки':
        msg = random.choice(vup_slouki_links)
        bot.send_message(message.chat.id, msg)
    elif message.text == 'Сочкники':
        msg = random.choice(vup_sochniki_links)
        bot.send_message(message.chat.id, msg)
    elif message.text == 'Куличи':
        msg = random.choice(vup_kylichi_links)
        bot.send_message(message.chat.id, msg)
    elif message.text == 'Плюшки':
        msg = random.choice(vup_plywki_links)
        bot.send_message(message.chat.id, msg)
    elif message.text == 'Блинчики':
        msg = random.choice(vup_blinchki_links)
        bot.send_message(message.chat.id, msg)

    elif message.text == 'Овощной':
        msg = random.choice(salat_ovowi_links)
        bot.send_message(message.chat.id, msg)
    elif message.text == 'Мясной':
        msg = random.choice(salat_myasnoi_links)
        bot.send_message(message.chat.id, msg)
    elif message.text == 'Рыбный':
        msg = random.choice(salat_rubnui_links)
        bot.send_message(message.chat.id, msg)
    elif message.text == 'Смешаный':
        msg = random.choice(salat_smewanui_links)
        bot.send_message(message.chat.id, msg)

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши /start")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True)
