from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

from routers.admin_router import router as admin_rout
from routers.post_router import router as post_rout

dp = Dispatcher()
dp.include_router(admin_rout)
dp.include_router(post_rout)
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)

#.\.venv\Scripts\Activate.ps1


TOKEN = "8799240440:AAFNztn1WEwFcOpl-ABse4xqJgop7EMiARg"
bot = Bot(token=TOKEN)







async def main(): #запуск LongPolling
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__": #Проверка main/name
    asyncio.run(main())
