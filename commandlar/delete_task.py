# commands/delete_task.py
from aiogram import types, Router,F

from button import commandalar
from commandlar.add_task import user_tasks  # Vazifalarni olish uchun

router = Router()

@router.message(F.text == "O'chirish🗑")
async def delete_task_prompt(message: types.Message):
    user_id = message.from_user.id
    tasks = user_tasks.get(user_id, [])

    if not tasks:
        await message.reply("Sizda hech qanday vazifa yo'q.")
    else:
        task_list = "\n".join(f"{i + 1}. {task}" for i, task in enumerate(tasks))
        await message.reply(f"Qaysi vazifani o'chirmoqchisiz? Raqamini kiriting:\n{task_list}")


@router.message(lambda message: message.text.isdigit())
async def process_delete_task(message: types.Message):
    print(message.text)
    user_id = message.from_user.id
    tasks = user_tasks.get(user_id, [])
    task_number = int(message.text) - 1

    if 0 <= task_number < len(tasks):
        deleted_task = tasks.pop(task_number)
        await message.reply(f"Vazifa o'chirildi: {deleted_task}",reply_markup=commandalar)
    else:
        await message.reply("Noto'g'ri raqam. Iltimos, to'g'ri vazifa raqamini kiriting.")
