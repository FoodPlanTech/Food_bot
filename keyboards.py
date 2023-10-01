from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from requests_for_bot import get_preferences, get_subscribtions



# from requests_for_bot import get_preferences
import requests

racion_id_buttons=[]
subscribtion_id_buttons=[]
subscription_price=[]
amount_id_buttons=[]


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


amount = [{'id': 1, 'title': 'Белая'},
          {'id': 2, 'title': 'Синяя'},
          {'id': 3, 'title': 'Красная'},
          ]
amount_list =[]
for quantity in amount:
        amount_id_buttons.append(f'quantity{quantity["id"]}')
        amount_list.append([InlineKeyboardButton(text=quantity['title'], callback_data=f'quantity{quantity["id"]}')])
        select_dishes = InlineKeyboardMarkup(inline_keyboard=amount_list)
select_dishes = select_dishes

# select_dishes = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(
#             text='Белая',
#             callback_data='period'
#         )
#     ],
#     [
#         InlineKeyboardButton(
#             text='Синяя',
#             callback_data='period'
#         )
#     ],
#     [
#         InlineKeyboardButton(
#             text='Красная',
#             callback_data='period'
#         )
#     ]
# ])

select_rating = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Like',
            callback_data='like'
        )
    ],
     [
        InlineKeyboardButton(
            text='Dislike',
            callback_data='dislike'
        )
    ]
])

preferences = get_preferences()
preferences_list =[]
for pref in preferences:
        racion_id_buttons.append(f'pref{pref["id"]}')
        preferences_list.append([InlineKeyboardButton(text = pref['title'], callback_data = f'pref{pref["id"]}')])
        racion_kb = InlineKeyboardMarkup(inline_keyboard = preferences_list)
select_racion = racion_kb

# one_dish = InlineKeyboardButton('Белая', callback_data='period')
# two_dishes = InlineKeyboardButton('Синяя', callback_data='period')
# three_dishes = InlineKeyboardButton('Красная', callback_data='period') 
# dishes_kb = InlineKeyboardMarkup(resize_keyboard=True).add(one_dish, two_dishes, three_dishes)


subscribtions = get_subscribtions()
subscribtions_list = []
for subscription in subscribtions:
        subscribtion_id_buttons.append(f"sub{subscription['id']}")
        subscription_price.append(subscription['price']["amount"])
        subscribtions_list.append([InlineKeyboardButton(text=subscription['title'], callback_data=f"sub{subscription['id']}")])
        period = InlineKeyboardMarkup(inline_keyboard=subscribtions_list)
select_period = period

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text='Получить рецепт')
keyboard.add(button_1)