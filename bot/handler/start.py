from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.button.reply import customer_menu, login_register, merchant_menu
from bot.dispacher import dp
from db.DTO import MerchantDto, ClientDto
from db.model import Merchants, Clients


@dp.message_handler(commands='start')
async def main_handler(msg: types.Message, state :FSMContext):
    print(1)

    merchant = Merchants().select(user_id = str(msg.from_user.id)).fetchone()
    client = Clients().select(user_id = str(msg.from_user.id)).fetchone()

    if merchant or client:
        if merchant:
            merchant = MerchantDto(*merchant)
            await msg.answer(f"Assalomu alaykum {merchant.full_name}" , reply_markup=merchant_menu())
        else:
            client = ClientDto(*client)
            await msg.answer(f"Assalomu alaykum {client.fullname}", reply_markup=customer_menu())
    else:
        await state.set_state('login_register')
        await msg.answer("Login   Register"  , reply_markup=login_register())




