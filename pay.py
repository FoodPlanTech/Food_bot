from aiogram import Bot, types
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery
from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv
import os
from keyboards import select_recipe
from requests_for_bot import send_subscriber_information


load_dotenv()
bot = Bot(token=os.environ['TELEGRAM_TOKEN'])
dp = Dispatcher(bot)

async def process_callback_subscribe(cb_query: types.CallbackQuery):
    await bot.send_invoice(
        chat_id=cb_query.message.chat.id,
        title='Подписка',
        description='Оформляем подписку на канал',
        payload='Покупа через Телеграм бот',
        provider_token=os.environ['PROVIDER_TOKEN'],
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

async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

async def successfull_payment(message: Message):
    purchase_message = message.successful_payment.to_python()
    send_subscriber_information()
    purchase_message['user_id'] = message.from_user.id
    await message.answer(f'Спасибо за оплату {message.successful_payment.total_amount // 100} {message.successful_payment.currency}.', reply_markup=select_recipe)
