from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InputFile, InputMedia

from aiogram.types import Message, LabeledPrice, PreCheckoutQuery, ContentType
import random
from dotenv import load_dotenv
import os
# Здесь лишнее нужно будет убрать
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
# import requests

# resp = requests.get('http://v1131340.hosted-by-vdsina.ru:5555/api/v1/recipes/')
# print(resp.json())

click_counter = {}

load_dotenv() 
bot = Bot(token=os.environ['TELEGRAM_TOKEN'])
dp = Dispatcher(bot)   
foods_photo = ['eda.jpg', 'eda2.jpg','eda3.jpg']
foods_recipe = ['ПОКУШАЕМ?','ВКУСНО ПОКУШАЕМ?','ОЧЕНЬ ВКУСНО ПОКУШАЕМ?']
photo = InputFile(foods_photo[0])
subscribe = InlineKeyboardButton('Оформить подписку', callback_data='subscribe')
new_recipe = InlineKeyboardButton('Новый рецепт', callback_data='new_recipe')
welcome_buttons = InlineKeyboardMarkup(resize_keyboard=True).add(subscribe, new_recipe)

# Первые сообщения для клиента--------
@dp.message_handler(commands=['start']) # Вывод сообщений после /start
async def process_start_command(message: types.Message):
    await message.reply("Добро пожаловать в супер-пупер бот. Мы подберем Вам рецепт")
    await bot.send_photo(message.from_user.id, photo, caption='Рецепт для вас', reply_markup=welcome_buttons)
    click_counter['new_recipe'] = 2

@dp.callback_query_handler(lambda c: c.data == 'new_recipe')# Отзыв на вторую кнопку. После 3 раз крашится. Надо исправлять
async def process_callback_new_recipe(call: types.CallbackQuery):
    file_path = InputFile(foods_photo[click_counter['new_recipe']])
    recipe = foods_recipe[click_counter['new_recipe']]
    file = InputMedia(media=file_path, caption=recipe)
    if click_counter['new_recipe'] == 1:
        await call.message.edit_media(file,reply_markup=InlineKeyboardMarkup(resize_keyboard=True).add(subscribe))
    else:
        await call.message.edit_media(file,reply_markup=welcome_buttons)
    click_counter['new_recipe'] -= 1

#---------------------

# ВСЕ ПО ОПЛАТЕ--------
@dp.pre_checkout_query_handler(lambda query: True)# Процесс оплаты
async def pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.callback_query_handler(lambda c: c.data == 'subscribe')# Первая кнопка. Покупка
async def process_callback_subscribe(call: types.CallbackQuery):
    await bot.send_invoice(
    chat_id=call.message.chat.id,
    title='Подписка',
    description='Оформляем подписку на канал',
    payload='Покупа через Телеграм бот',
    provider_token= os.environ['PROVIDER_TOKEN'],
    currency='rub',
    prices=[
        LabeledPrice(
            label='Подписка на канал',
            amount=10000 
        )
    ],
    max_tip_amount=500,
    start_parameter="one_month_sub",
    need_name=True,
    need_email=True,
    need_phone_number=True,
    need_shipping_address=False,
    send_phone_number_to_provider=False,
    send_email_to_provider=False,
    is_flexible=False,
    disable_notification=False,
    protect_content=False,
    reply_to_message_id=None,
    allow_sending_without_reply=True,
    reply_markup=None
)

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT) # Процесс после оплаты
async def successfull_payment(message: Message):
    purchase_message = message.successful_payment.to_python()
    for key, val in purchase_message.items():
        print(f'{key} = {val}')
    msg = f'Спасибо за оплату {message.successful_payment.total_amount // 100} {message.successful_payment.currency}.'
    await message.answer(msg)
# Оплата кончилась------
    

if __name__ == '__main__':  
    executor.start_polling(dp)
    