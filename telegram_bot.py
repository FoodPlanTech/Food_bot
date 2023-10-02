from aiogram import Bot
from aiogram.dispatcher import Dispatcher, filters
from aiogram.utils import executor
from aiogram.types import ContentType
from dotenv import load_dotenv
import os
from pay import process_callback_subscribe, pre_checkout_query,\
      successfull_payment
from basics import choose_calories, process_start_command,\
    process_callback_new_recipe, choose_amount, choose_period,\
    choose_racion,choose_recipe, set_rating
from keyboards import racion_id_buttons, subscribtion_id_buttons, amount_id_buttons

load_dotenv()
bot = Bot(token=os.environ['TELEGRAM_TOKEN'])
dp = Dispatcher(bot)

dp.register_message_handler(process_start_command, commands='start')
dp.register_callback_query_handler(process_callback_new_recipe, lambda c: c.data == 'new_recipe')
dp.register_callback_query_handler(choose_calories, lambda c: c.data == 'subscribe')
dp.register_callback_query_handler(choose_racion, lambda c: c.data == 'racion_kb')
dp.register_callback_query_handler(choose_amount, lambda c: c.data in racion_id_buttons)
dp.register_callback_query_handler(choose_period, lambda c: c.data in amount_id_buttons)
dp.register_callback_query_handler(process_callback_subscribe, lambda c: c.data in subscribtion_id_buttons)
dp.register_pre_checkout_query_handler(pre_checkout_query, lambda query: True)
dp.register_message_handler(successfull_payment, content_types=ContentType.SUCCESSFUL_PAYMENT)
dp.register_message_handler(choose_recipe, lambda c: c.text =='Получить рецепт')
dp.register_callback_query_handler(set_rating, lambda c: c.data in ['like', 'dislike'])


if __name__ == '__main__':
    executor.start_polling(dp)