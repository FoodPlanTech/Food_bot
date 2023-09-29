from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from requests_for_bot import get_preferences
import requests



a=InlineKeyboardButton('до 1500', callback_data='racion_kb')
b=InlineKeyboardButton('до 2500', callback_data='racion_kb')
с=InlineKeyboardButton('больше 2500', callback_data='racion_kb') 
calories_kb = InlineKeyboardMarkup(resize_keyboard=True).add(a,b,с)

vegan_dishes = InlineKeyboardButton('Вегитарианское меню', callback_data='dishes_kb')
meat_dishes = InlineKeyboardButton('Сытно и полезно', callback_data='dishes_kb')
joy_dishes = InlineKeyboardButton('Быстро и вкусно', callback_data='dishes_kb') 
racion_kb = InlineKeyboardMarkup(resize_keyboard=True).add(vegan_dishes, meat_dishes, joy_dishes)

preferences = get_preferences()
preferences_list =[]
for pref in preferences:
        preferences_list.append([InlineKeyboardButton(text = pref['title'], callback_data = pref['id'])])
        racion_kb = InlineKeyboardMarkup(inline_keyboard = preferences_list)
        print(racion_kb)
select_racion = racion_kb

one_dish = InlineKeyboardButton('Белая', callback_data='period')
two_dishes = InlineKeyboardButton('Синяя', callback_data='period')
three_dishes = InlineKeyboardButton('Красная', callback_data='period') 
dishes_kb = InlineKeyboardMarkup(resize_keyboard=True).add(one_dish, two_dishes, three_dishes)

one_month = InlineKeyboardButton('1 мес', callback_data='payment') #колбэк на кнопку с оплатой
three_monthes = InlineKeyboardButton('3 мес', callback_data='payment')
six_monthes = InlineKeyboardButton('6 мес', callback_data='payment') 
period = InlineKeyboardMarkup(resize_keyboard=True).add(one_month, three_monthes, six_monthes)