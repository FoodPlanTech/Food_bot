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

def main():
    load_dotenv() 
    bot = Bot(token=os.environ['TELEGRAM_TOKEN'])
    dp = Dispatcher(bot)   
    foods = ['eda.jpg', 'eda2.jpg','eda3.jpg']
    photo = InputFile(foods[0])
    subscribe = InlineKeyboardButton('Оформить подписку', callback_data='subscribe')
    new_recipe = InlineKeyboardButton('Новый рецепт', callback_data='new_recipe')
    welcome_buttons = InlineKeyboardMarkup(resize_keyboard=True).add(subscribe, new_recipe)

    @dp.pre_checkout_query_handler(lambda query: True)# Это мне для оплаты
    async def pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
        await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=False, error_message='Что-то не так')


    @dp.callback_query_handler(lambda c: c.data == 'subscribe')# Первая кнопка. Покупка
    async def process_callback_subscribe(call: types.CallbackQuery):
        await bot.send_invoice(
        chat_id=call.message.chat.id,
        title='Покупа через Телеграм бот',
        description='Проверка работы',
        payload='Что эТО??',
        provider_token='381764678:TEST:67486',
        currency='rub',
        prices=[
            LabeledPrice(
                label='Подписка на канал',
                amount=35000 
            )
        ],
        max_tip_amount=500,
        start_parameter='Pin_kod',
        provider_data=None,
        # photo_url='picture_for_pay.jpg',
        photo_size=100,
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

    @dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT) # Это моё после оплаты
    async def successfull_payment(message: Message):
        msg = f'Спасибо за оплату {message.successful_payment.total_amount // 100} {message.successful_payment.currency}.'
        await message.answer(msg)

    @dp.callback_query_handler(lambda c: c.data == 'new_recipe')# Отзыв на вторую кнопку. После 3 раз крашится. Надо исправлять
    async def process_callback_new_recipe(call: types.CallbackQuery):
        subscribe = InlineKeyboardButton('Оформить подписку', callback_data='subscribe')# 30,31,32 Строки возможно лишние. Надо тестить
        new_recipe = InlineKeyboardButton('Новый рецепт', callback_data='new_recipe')
        welcome_buttons = InlineKeyboardMarkup(resize_keyboard=True).add(subscribe, new_recipe)
        file_path = InputFile(random.sample(foods, 1)[0])
        file = InputMedia(media=file_path, caption="Updated caption :)")
        await call.message.edit_media(file,reply_markup=welcome_buttons)

    @dp.message_handler(commands=['start']) # Вывод сообщений после /start
    async def process_start_command(message: types.Message):
        await message.reply("Добро пожаловать в супер-пупер бот. Мы подберем Вам рецепт")
        await bot.send_photo(message.from_user.id, photo, caption='Рецепт для вас', reply_markup=welcome_buttons)

    executor.start_polling(dp)

if __name__ == '__main__':  
    main()
    