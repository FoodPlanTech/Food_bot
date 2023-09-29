from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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
