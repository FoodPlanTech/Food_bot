from aiogram import Bot, types
from keyboards import select_start_buttons, select_calories, select_racion, select_dishes, select_period, select_rating
from requests_for_bot import get_recipes, send_id, send_rating
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InputFile, InputMedia
import requests
import urllib.request
import os
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv



remember_choice={}
click_counter = {}
recipe_id =[]

load_dotenv()
bot = Bot(token=os.environ['TELEGRAM_TOKEN'])
dp = Dispatcher(bot)
def get_card(telegram_id, bool):
    nl = '\n'
    if bool:
        recipe = get_recipes(telegram_id)
        recipe_id.append(recipe['id'])
    # ' 30 калорий ' + ingredient['price'] + ' ' + ingredient['price_currency']
        text = f"{recipe['title']}\n"\
        f"Инструкция приготовления:\n"\
        f"{recipe['guide']}\n"\
        f'Ингредиенты:\n'\
        f"{''.join([ingredient['title']  + nl for ingredient in recipe['ingredients']])}"
        imgURL = recipe['image']
        urllib.request.urlretrieve(imgURL, "./media/local-filename.jpg")# Надо не только Jpg сделать
    else:
        recipe = get_recipes(None)
    #' 30 калорий ' + ingredient['price'] + ' ' + ingredient['price_currency'] +
        text = f"{recipe[click_counter['new_recipe']]['title']}\n"\
        f"Инструкция приготовления:\n"\
        f"{recipe[click_counter['new_recipe']]['guide']}\n"\
        f'Ингредиенты:\n'\
        f"{''.join([ingredient['title'] +  nl for ingredient in recipe[click_counter['new_recipe']]['ingredients']])}"
        imgURL = recipe[click_counter['new_recipe']]['image']
        urllib.request.urlretrieve(imgURL, "./media/local-filename.jpg")# Надо не только Jpg сделать
    return text


async def process_callback_new_recipe(cb_query: types.CallbackQuery):
    text = get_card(cb_query.from_user.id, False)
    subscribe = InlineKeyboardButton('Оформить подписку', callback_data='subscribe')
    file = InputMedia(media=InputFile("./media/local-filename.jpg"), caption=text)
    if click_counter['new_recipe'] == 0:
        await cb_query.message.edit_media(file, reply_markup=InlineKeyboardMarkup(resize_keyboard=True).add(subscribe))
    else:
        await cb_query.message.edit_media(file, cb_query['message']['reply_markup'])
    click_counter['new_recipe'] -= 1


async def process_start_command(message: types.Message):
    await message.answer("Добро пожаловать в FoodPlan бот! \nУ нас есть для вас тысячи рецептов блюд на любой вкус.\n"\
                        "С подпиской на наш сервис вам больше не придется думать о том, что приготовить, это мы берем на себя!")
    click_counter['new_recipe'] = 2
    text = get_card(message.from_user.id, False)
    await bot.send_photo(message.from_user.id, photo=open("./media/local-filename.jpg",'rb'), caption=text, reply_markup=select_start_buttons)
    click_counter['new_recipe'] -= 1
    telegram_id = message.from_user.id
    send_id(telegram_id)

async def choose_calories(cb_query: types.CallbackQuery):
    await cb_query.message.answer('Выберите желаемую калорийность', reply_markup=select_calories)


async def choose_racion(cb_query: types.CallbackQuery):
    await cb_query.message.answer('Выберите рацион', reply_markup=select_racion)


async def choose_amount(cb_query: types.CallbackQuery):
    await cb_query.message.answer('Мы предлагаем вам 3 варианта подписки и выберите количество рецептов ...', reply_markup=select_dishes)
    preference_ids = cb_query.data
    remember_choice['preference_ids'] = preference_ids


async def choose_period(cb_query: types.CallbackQuery):
    await cb_query.message.answer('Выберите срок и описываем 1месяц за 150р и тд', reply_markup=select_period)

async def choose_recipe(cb_query: types.CallbackQuery):
    text = get_card(cb_query.from_user.id, True)
    await bot.send_photo(cb_query.from_user.id, photo=open("./media/local-filename.jpg",'rb'), caption=text, reply_markup=select_rating)

async def set_rating(cb_query: types.CallbackQuery):
    inner_buttons = []
    for inline_keyboard in cb_query.message.reply_markup.inline_keyboard:
        if inline_keyboard[0]['callback_data'] == cb_query.data:
            inner_buttons.append(inline_keyboard[0])
    await bot.edit_message_reply_markup(cb_query.message.chat.id, cb_query.message.message_id, reply_markup=InlineKeyboardMarkup(resize_keyboard=True).add(inner_buttons[0]))
    send_rating(cb_query.data, cb_query.from_user.id, recipe_id.pop())

if __name__ == '__main__':  
    executor.start_polling(dp)
    