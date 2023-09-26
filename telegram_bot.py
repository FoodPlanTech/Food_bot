from aiogram import Bot, types 
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InputFile, InputMedia
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

    @dp.callback_query_handler(lambda c: c.data == 'subscribe')# Отзыв на первую кнопку
    async def process_callback_subscribe(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')

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
    