# commands/add_task.py
from aiogram import types, Router,F
from button import commandalar, recommend

# Router orqali registratsiya qilamiz
router = Router()

# Vazifalarni saqlash uchun lug'at va vazifani kutish ro'yxati
user_tasks = {}
awaiting_task_input = set()

@router.message(F.text == "Vazifa qo'shish✅")
async def add_task_prompt(message: types.Message):
    await message.reply("Iltimos, vazifani kiriting:")
    awaiting_task_input.add(message.from_user.id)  # Foydalanuvchini kutish ro'yxatiga qo'shamiz

@router.message(lambda message: message.from_user.id in awaiting_task_input)
async def process_task(message: types.Message):
    user_id = message.from_user.id
    if user_id in awaiting_task_input:
        task_text = message.text
        print(task_text)
        if user_id not in user_tasks:
            user_tasks[user_id] = []
        user_tasks[user_id].append(task_text)

        await message.reply(f"Siz kiritgan vazifa: {task_text}\nVazifa muvaffaqiyatli saqlandi!\n\nVazifani eslatish kerakmi?",reply_markup=recommend)
        awaiting_task_input.remove(user_id)
