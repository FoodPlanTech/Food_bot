from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from requests_for_bot import get_preferences
import requests



select_start_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            'Оформить подписку',
            callback_data='subscribe'
        )
    ],
    [
        InlineKeyboardButton(
            'Новый рецепт',
            callback_data='new_recipe'
        )
    ]
])

select_calories = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='До 1500',
            callback_data='racion_kb'
        )
    ],
    [
        InlineKeyboardButton(
            text='До 2500',
            callback_data='racion_kb'
        )
    ],
    [
        InlineKeyboardButton(
            text='Больше 2500',
            callback_data='racion_kb'
        )
    ],
])

select_racion = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Вегитарианское меню',
            callback_data='dishes_kb'
        )
    ],
    [
        InlineKeyboardButton(
            text='Сытно и полезно',
            callback_data='dishes_kb'
        )
    ],
    [
        InlineKeyboardButton(
            text='Быстро и вкусно',
            callback_data='dishes_kb'
        )
    ]
])

select_dishes = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Белая',
            callback_data='period'
        )
    ],
    [
        InlineKeyboardButton(
            text='Синяя',
            callback_data='period'
        )
    ],
    [
        InlineKeyboardButton(
            text='Красная',
            callback_data='period'
        )
    ]
])

preferences = get_preferences()
preferences_list =[]
for pref in preferences:
        preferences_list.append([InlineKeyboardButton(text = pref['title'], callback_data = 'dishes_kb')])
        racion_kb = InlineKeyboardMarkup(inline_keyboard = preferences_list)
select_racion = racion_kb


select_period = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='1 мес',
            callback_data='payment'
        )
    ],
    [
        InlineKeyboardButton(
            text='3 мес',
            callback_data='payment'
        )
    ],
    [
        InlineKeyboardButton(
            text='6 мес',
            callback_data='payment'
        )
    ]
])
