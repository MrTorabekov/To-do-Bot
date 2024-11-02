from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

all_command = [
    [KeyboardButton(text="Vazifa qo'shish✅"), KeyboardButton(text="O'chirish🗑")],
    [KeyboardButton(text="Vazifalar📋"), KeyboardButton(text="Eslatish vaqti⏰")]
]

commandalar = ReplyKeyboardMarkup(keyboard=all_command, resize_keyboard=True)

recommendation = [
    [KeyboardButton(text="Ha"), KeyboardButton(text="Yo'q")]
]
recommend = ReplyKeyboardMarkup(keyboard=recommendation, resize_keyboard=True)
