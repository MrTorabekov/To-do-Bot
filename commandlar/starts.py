from aiogram import types, Router
from aiogram.filters import Command
from button import commandalar

router = Router()

@router.message(Command("start"))
async def add_task_prompt(message: types.Message):
    await message.reply(f"Salom xush kelibsiz{message.from_user.full_name}.\nO'zingizga kerakli bo'limni tanlang!",reply_markup=commandalar)