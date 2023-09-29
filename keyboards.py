from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
<<<<<<< Updated upstream
=======
# from requests_for_bot import get_preferences
import requests


>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
=======
select_recipe = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Получить рецент',
            callback_data='recipe'
        )
    ]
])


# preferences = get_preferences()
# preferences_list =[]
# for pref in preferences:
#         preferences_list.append([InlineKeyboardButton(text = pref['title'], callback_data = pref['id'])])
#         racion_kb = InlineKeyboardMarkup(inline_keyboard = preferences_list)
#         print(racion_kb)
# select_racion = racion_kb

# one_dish = InlineKeyboardButton('Белая', callback_data='period')
# two_dishes = InlineKeyboardButton('Синяя', callback_data='period')
# three_dishes = InlineKeyboardButton('Красная', callback_data='period') 
# dishes_kb = InlineKeyboardMarkup(resize_keyboard=True).add(one_dish, two_dishes, three_dishes)


>>>>>>> Stashed changes
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
