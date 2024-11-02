# commands/show_tasks.py
from aiogram import types, Router
from aiogram.filters import Command
from aiogram import F
from commandlar.add_task import user_tasks  # Vazifalarni olish uchun

router = Router()

@router.message(F.text == "Vazifalar📋")
async def show_tasks(message: types.Message):
    user_id = message.from_user.id
    tasks = user_tasks.get(user_id, [])

    if not tasks:
        await message.reply("Sizda hech qanday vazifa yo'q.")
    else:
        task_list = "\n".join(f"{i + 1}. {task}" for i, task in enumerate(tasks))
        await message.reply(f"Sizning vazifalaringiz:\n{task_list}")
