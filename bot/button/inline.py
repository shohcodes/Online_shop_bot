from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def role_inline_btn():
    design = [
        [InlineKeyboardButton("CLIENT", callback_data='CLIENT'),
         InlineKeyboardButton("MERCHANT ", callback_data='MERCHANT')]
    ]

    return InlineKeyboardMarkup(inline_keyboard=design)
