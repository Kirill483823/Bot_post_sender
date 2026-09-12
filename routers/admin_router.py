from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command
from keyboards.kb_main import create_post_keyb


router = Router()

ADMINS_ID = [5157719233]

@router.message(Command("start")) #главное меню со старта и проверка на админа
async def st_cmd(message: Message):
    if message.from_user.id in ADMINS_ID:
        await message.answer(
            "👋 Привет, ты находишься в боте для создания и редактирования постов для Telegram-канала"
            "\n\n🔩 Бот находится в разработке, так что при обнаружении багов или ошибок сообщи мне @kirill_r24",
            reply_markup=create_post_keyb
            )
    else:
        await message.answer("⛓️‍💥 Ты не входишь в число админов")


@router.callback_query(F.data == "create_post")
async def create_p(callback):
    await callback.answer()
    await callback.message.answer("📃Отправь пост:")
