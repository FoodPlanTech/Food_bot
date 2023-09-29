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


calories = [{'id': 1, 'text': 'до 1500'},
          {'id': 2, 'text': 'до 2500'},
          {'id': 3, 'text': 'от 2500'},]
#calories_keyboard = [[calorie['text']] for calorie in calories] пока непонятно 

def main():
    load_dotenv() 
    bot = Bot(token=os.environ['TELEGRAM_TOKEN'])
    dp = Dispatcher(bot)   
    #foods = ['eda.jpg', 'eda2.jpg','eda3.jpg']
    #photo = InputFile(foods[0])
    subscribe = InlineKeyboardButton('Оформить подписку', callback_data='subscribe')
    new_recipe = InlineKeyboardButton('Новый рецепт', callback_data='new_recipe')
    welcome_buttons = InlineKeyboardMarkup(resize_keyboard=True).add(subscribe, new_recipe)

    a=InlineKeyboardButton('до 1500', callback_data='racion_kb')
    b=InlineKeyboardButton('до 2500', callback_data='racion_kb')
    с=InlineKeyboardButton('больше 2500', callback_data='racion_kb') 
    calories_kb = InlineKeyboardMarkup(resize_keyboard=True).add(a,b,с)

    vegan_dishes = InlineKeyboardButton('Вегитарианское меню', callback_data='dishes_kb')
    meat_dishes = InlineKeyboardButton('Сытно и полезно', callback_data='dishes_kb')
    joy_dishes = InlineKeyboardButton('Быстро и вкусно', callback_data='dishes_kb') 
    racion_kb = InlineKeyboardMarkup(resize_keyboard=True).add(vegan_dishes, meat_dishes, joy_dishes)

    one_dish = InlineKeyboardButton('Белая', callback_data='period')
    two_dishes = InlineKeyboardButton('Синяя', callback_data='period')
    three_dishes = InlineKeyboardButton('Красная', callback_data='period') 
    dishes_kb = InlineKeyboardMarkup(resize_keyboard=True).add(one_dish, two_dishes, three_dishes)

    one_month = InlineKeyboardButton('1 мес', callback_data='payment') #колбэк на кнопку с оплатой
    three_monthes = InlineKeyboardButton('3 мес', callback_data='payment')
    six_monthes = InlineKeyboardButton('6 мес', callback_data='payment') 
    period = InlineKeyboardMarkup(resize_keyboard=True).add(one_month, three_monthes, six_monthes)



    





    @dp.message_handler(commands=['start']) # Вывод сообщений после /start
    async def process_start_command(message: types.Message):
        await message.reply("Добро пожаловать в супер-пупер бот. Мы подберем Вам рецепт")
        #await bot.send_photo(message.from_user.id, photo, caption='Рецепт для вас', reply_markup=welcome_buttons) 
        await bot.send_message(message.from_user.id, 'Рецепт для вас', reply_markup=welcome_buttons)





    @dp.callback_query_handler(lambda c: c.data == 'subscribe')
    async def choose_calories(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id , 'Выберете желаемую калорийность', reply_markup=calories_kb)

    
    @dp.callback_query_handler(lambda c: c.data == 'racion_kb')
    async def choose_racion(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id , 'Выберете рацион', reply_markup=racion_kb)


    @dp.callback_query_handler(lambda c: c.data == 'dishes_kb')
    async def choose_amount(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id , 'Мы предлагаем вам 3 варианта подписки и описываем каждую...', reply_markup=dishes_kb)


    @dp.callback_query_handler(lambda c: c.data == 'period')
    async def choose_period(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id , 'Выберете срок и описываем 1месяц за 150р и тд', reply_markup=period)


    executor.start_polling(dp)

if __name__ == '__main__':  
    main()
    
