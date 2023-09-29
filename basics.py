from aiogram import Bot, types
from keyboards import select_start_buttons, select_calories, select_racion, select_dishes, select_period
from requests_for_bot import get_recipes
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InputFile, InputMedia
import requests
import urllib.request
import os
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor



click_counter = {}
bot = Bot(token=os.environ['TELEGRAM_TOKEN'])
dp = Dispatcher(bot)
def get_card(id):
    nl = '\n'
    if id:
        id = 123123123
    recipe = get_recipes(id)
    print(recipe)
    print(click_counter['new_recipe'])
    if id:
        text = f"{recipe['title']}\n"\
        f"Инструкция приготовления:\n"\
        f"{recipe['guide']}\n"\
        f'Ингредиенты:\n'\
        f"{''.join([ingredient['title'] + ' 30 калорий ' + ingredient['price'] + ' ' + ingredient['price_currency'] + nl for ingredient in recipe['ingredients']])}"
        # imgURL = recipe['image']
        # print(imgURL)
    else:
        text = f"{recipe[click_counter['new_recipe']]['title']}\n"\
        f"Инструкция приготовления:\n"\
        f"{recipe[click_counter['new_recipe']]['guide']}\n"\
        f'Ингредиенты:\n'\
        f"{''.join([ingredient['title'] + ' 30 калорий ' + ingredient['price'] + ' ' + ingredient['price_currency'] + nl for ingredient in recipe[click_counter['new_recipe']]['ingredients']])}"
        imgURL = recipe[click_counter['new_recipe']]['image']
        urllib.request.urlretrieve(imgURL, "local-filename.jpg")# Надо не только Jpg сделать
    return text


async def process_callback_new_recipe(cb_query: types.CallbackQuery):
    text = get_card(None)
    subscribe = InlineKeyboardButton('Оформить подписку', callback_data='subscribe')
    file = InputMedia(media=InputFile('local-filename.jpg'), caption=text)
    if click_counter['new_recipe'] == 0:
        await cb_query.message.edit_media(file, reply_markup=InlineKeyboardMarkup(resize_keyboard=True).add(subscribe))
    else:
        await cb_query.message.edit_media(file, cb_query['message']['reply_markup'])
    click_counter['new_recipe'] -= 1


async def process_start_command(message: types.Message):
    await message.answer("Добро пожаловать в FoodPlan бот! \nУ нас есть для вас тысячи рецептов блюд на любой вкус.\n"\
                        "С подпиской на наш сервис вам больше не придется думать о том, что приготовить, это мы берем на себя!")
    click_counter['new_recipe'] = 1
    text = get_card(None)
    await bot.send_photo(message.from_user.id, photo=open("local-filename.jpg",'rb'), caption=text, reply_markup=select_start_buttons)
    click_counter['new_recipe'] -= 1
    url = 'http://v1131340.hosted-by-vdsina.ru:5555/api/v1/tg-accounts/'
    payload = {
    'telegram_id': message.from_user.id
        }
    response_post = requests.post(url, data=payload)
    response_post.raise_for_status()


async def choose_calories(cb_query: types.CallbackQuery):
    await cb_query.message.answer('Выберите желаемую калорийность', reply_markup=select_calories)


async def choose_racion(cb_query: types.CallbackQuery):
    await cb_query.message.answer('Выберите рацион', reply_markup=select_racion)


async def choose_amount(cb_query: types.CallbackQuery):
    await cb_query.message.answer('Мы предлагаем вам 3 варианта подписки и выберите количество рецептов ...', reply_markup=select_dishes)


async def choose_period(cb_query: types.CallbackQuery):
    await cb_query.message.answer('Выберите срок и описываем 1месяц за 150р и тд', reply_markup=select_period)

async def choose_recipe(cb_query: types.CallbackQuery):
    await cb_query.message.answer(get_card(cb_query.message.from_user.id))


if __name__ == '__main__':  
    executor.start_polling(dp)
    