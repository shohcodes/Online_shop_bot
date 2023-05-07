from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from bot.button.text import *


def customer_menu():
    design = [
        [cust_shop_text , cust_cart_text],
        [cust_account_text , cust_contactus_text],
    ]
    return ReplyKeyboardMarkup(keyboard=design , resize_keyboard=True , one_time_keyboard=True)

def merchant_menu():
    design=[
        [mer_product_text , mer_sales_text],
        [mer_account_text , mer_contact_text]
    ]
    return ReplyKeyboardMarkup(keyboard=design , resize_keyboard=True , one_time_keyboard=True)

def login_register():
    design = [
        [login, register]
    ]
    return ReplyKeyboardMarkup(keyboard=design , resize_keyboard=True , one_time_keyboard=True)

def phone_btn():
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(phone, request_contact=True)]], resize_keyboard=True)
