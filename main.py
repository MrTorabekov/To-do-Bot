import asyncio
import logging
from aiogram import Bot, Dispatcher
from commandlar.add_task import router as add_task_router
from commandlar.delete_task import router as delete
from commandlar.starts import router as starts
from commandlar.show_task import router as show
from commandlar.remind_task import router as remind
TOKEN = "6862275470:AAGhci9BbBkGQ_5gzcXolyGSDXqjGlcKvLw"

dp = Dispatcher()


dp.include_router(add_task_router)
dp.include_router(starts)
dp.include_router(delete)
dp.include_router(show)
dp.include_router(remind)

async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    asyncio.run(main())
