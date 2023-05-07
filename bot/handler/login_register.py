import time
from time import strftime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from bot.button.inline import role_inline_btn
from bot.button.reply import phone_btn
from bot.button.text import register
from bot.dispacher import dp
from db.model import Merchants


@dp.message_handler(state = "login_register")
async def login_register_handler(msg: types.Message , state : FSMContext):
    if msg.text == register:
        await state.set_state('role_set')
        await msg.answer('Choose enter role : ', reply_markup=role_inline_btn())
    else:
        pass

# ==================== register -==========================


@dp.callback_query_handler(state = 'role_set')
async def role_inline_handler(call : types.CallbackQuery , state : FSMContext):
    await call.message.delete()
    async with state.proxy() as data:
        data['role'] = call.data
        data['user_id'] = str(call.message.from_user.id)
    await state.set_state('fullname_set')
    await call.message.answer('Enter your fullname : ')

@dp.message_handler(state = 'fullname_set')
async def register_handler(msg : types.Message , state :FSMContext):
    if len(msg.text.split()) >= 2:
        async with state.proxy() as data:
            data['fullname'] = msg.text
        await state.set_state('phone_set')
        await msg.answer('Send phone number 👇🏿: ', reply_markup=phone_btn())
    else:
        await msg.delete()
        await msg.answer('Fullname bad answer ❌!\nEXAMPLE : John Carl ✅')

@dp.message_handler(content_types = types.ContentTypes.CONTACT , state = 'phone_set')
async def phone_handler(msg : types.Message , state : FSMContext):
    async with state.proxy() as data:
        data['phone'] = msg.contact.phone_number
    await state.set_state('email_set')
    await msg.answer('Enter your email : ' , reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state = 'email_set')
async def email_handler(msg : types.Message , state : FSMContext):
    if msg.text.endswith("@gmail.com"):
        async with state.proxy() as data:
            data['email'] = msg.text
        await state.set_state('password_set')
        await msg.answer('Enter your password: ', reply_markup=ReplyKeyboardRemove())
    else:
        await msg.delete()
        await msg.answer('Email bad answer ❌!\nEXAMPLE : admin@gmail.com ✅')


@dp.message_handler(state = 'password_set')
async def phone_handler(msg : types.Message , state : FSMContext):
    async with state.proxy() as data:
        data['password'] = msg.text
        data['status'] = 'ACTIVE'
        data['created_at'] =strftime("%Y-%m-%d %H:%M")
    if data['role'] == 'MERCHANT':
        await state.set_state('card_number')
        await msg.answer('Enter your card number: ', reply_markup=ReplyKeyboardRemove())
    else:
        pass

@dp.message_handler(state = 'card_number')
async def card_number(msg : types.Message , state : FSMContext):
    card_num = "".join(msg.text.split())
    if not (card_num[:4] in ("8600" , "9860" , "4073" , "4455" , "6262") and len(card_num) == 16):
        await msg.delete()
        await msg.answer('Card Number bad answer ❌!\nEXAMPLE : 8600 1234 5678 9012 ✅')
    else:
        async with state.proxy() as data:
            data['card_number'] = card_num
        data = dict(data)
        del data['role']
        Merchants().insert_into(**data)
        await state.finish()
































# ==================== login -=============================