from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ContentType
from dotenv import load_dotenv
import os
from pay import process_callback_subscribe, pre_checkout_query,\
      successfull_payment
from basics import choose_calories, process_start_command,\
    process_callback_new_recipe, choose_amount, choose_period, choose_racion,choose_recipe
from keyboards import racion_id_buttons, subscribtion_id_buttons

load_dotenv()
bot = Bot(token=os.environ['TELEGRAM_TOKEN'])
dp = Dispatcher(bot)
print(subscribtion_id_buttons)
dp.register_message_handler(process_start_command, commands='start')
dp.register_callback_query_handler(process_callback_new_recipe, lambda c: c.data == 'new_recipe')
dp.register_callback_query_handler(choose_calories, lambda c: c.data == 'subscribe')
dp.register_callback_query_handler(choose_racion, lambda c: c.data == 'racion_kb')
dp.register_callback_query_handler(choose_amount, lambda c: c.data in racion_id_buttons)
dp.register_callback_query_handler(choose_period, lambda c: c.data == 'period')#
dp.register_callback_query_handler(process_callback_subscribe, lambda c: c.data in subscribtion_id_buttons)
dp.register_pre_checkout_query_handler(pre_checkout_query, lambda query: True)
dp.register_message_handler(successfull_payment, content_types=ContentType.SUCCESSFUL_PAYMENT)
dp.register_callback_query_handler(choose_recipe, lambda c: c.data == 'recipe')


if __name__ == '__main__':
    executor.start_polling(dp)

# ПОТОМ ПОНАДОБИТСЯ
# from aiogram.utils.exceptions import BotBlocked

# @dp.errors_handler(exception=BotBlocked)
# async def error_bot_blocked(update: types.Update, exception: BotBlocked):
#     # Update: объект события от Telegram. Exception: объект исключения
#     # Здесь можно как-то обработать блокировку, например, удалить пользователя из БД
#     print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")

#     # Такой хэндлер должен всегда возвращать True,
#     # если дальнейшая обработка не требуется.