from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from requests_for_bot import get_preferences, get_subscribtions



# from requests_for_bot import get_preferences
import requests

racion_id_buttons=[]

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

# select_racion = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(
#             text='Вегетерианское',
#             callback_data='dishes_kb1'
#         )
#     ],
#     [
#         InlineKeyboardButton(
#             text='Сытное',
#             callback_data='dishes_kb2'
#         )
#     ],
#     # [
#     #     InlineKeyboardButton(
#     #         text='Быстро и вкусно',
#     #         callback_data='dishes_kb'
#     #     )
#     # ]
# ])

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

select_recipe = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Получить рецент',
            callback_data='recipe'
        )
    ]
])


preferences = get_preferences()
preferences_list =[]
for pref in preferences:
        racion_id_buttons.append(str(pref['id']))
        preferences_list.append([InlineKeyboardButton(text = pref['title'], callback_data = pref['id'])])
        racion_kb = InlineKeyboardMarkup(inline_keyboard = preferences_list)
        print(racion_kb)
select_racion = racion_kb

# one_dish = InlineKeyboardButton('Белая', callback_data='period')
# two_dishes = InlineKeyboardButton('Синяя', callback_data='period')
# three_dishes = InlineKeyboardButton('Красная', callback_data='period') 
# dishes_kb = InlineKeyboardMarkup(resize_keyboard=True).add(one_dish, two_dishes, three_dishes)


subscribtions = get_subscribtions()
subscribtions_list = []
for subscription in subscribtions:
        #subscribtion_id_buttons.append(str(subscription['id']))
        subscribtions_list.append([InlineKeyboardButton(text=subscription['title'], callback_data=subscription['id'])])
        period = InlineKeyboardMarkup(inline_keyboard=subscribtions_list)
select_period = period

