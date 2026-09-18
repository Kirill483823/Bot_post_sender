import asyncio

from aiogram.types import Message
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from config import BOT_TOKEN
from Handlers import Handlers_router

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(Handlers_router)

#.\.venv\Scripts\Activate.ps1
#source .venv/Scripts/activate

async def main():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    asyncio.run(main())
