# commands/remind_task.py
from aiogram import types, Router, F
from datetime import datetime
from commandlar.add_task import user_tasks
import asyncio

from button import commandalar

router = Router()
user_reminders = {}


@router.message(F.text == "Eslatish vaqti⏰")
async def remind_task_prompt(message: types.Message):
    await message.reply(
        "Iltimos, vazifani va eslatish vaqtini HH:MM formatida kiriting. Masalan:\n\nVazifani bajarish - 14:30")

    @router.message(lambda message: "-" in message.text)
    async def set_reminder(message: types.Message):
        user_id = message.from_user.id
        print(message.text)
        try:
            # Vazifa va vaqtni ajratish
            task_text, task_time = map(str.strip, message.text.split("-"))
            task_time = datetime.strptime(task_time, "%H:%M").time()  # HH:MM formatini tekshirish

            # Vazifani saqlash
            if user_id not in user_tasks:
                user_tasks[user_id] = []
            user_tasks[user_id].append((task_text, task_time))

            await message.reply(f"✅ Vazifa qo'shildi: '{task_text}' soat {task_time.strftime('%H:%M')} da eslatiladi.",reply_markup=commandalar)

            # Eslatma vazifasini ishga tushirish
            asyncio.create_task(schedule_reminder(message, task_text, task_time))

        except ValueError:
            await message.reply("Iltimos, vaqtni to'g'ri formatda (HH:MM) kiriting.")

    async def schedule_reminder(message: types.Message, task_text, task_time):
        now = datetime.now().time()
        delay = (datetime.combine(datetime.today(), task_time) - datetime.combine(datetime.today(),
                                                                                  now)).total_seconds()

        # Agar vaqt kechikkan bo‘lsa, ertangi kun eslatiladi
        if delay < 0:
            delay += 86400  # 24 soat

        await asyncio.sleep(delay)  # Belgilangan vaqtgacha kutish
        await message.answer(f"⏰ Eslatma: {task_text}")
