from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from States.user_states import CreatePosts
from Keyboards.main_keyboards import create_post_keyb

router_start = Router()
ADMINS_IDS = [5157719233, 5511519564, 5676292004]

@router_start.message(CommandStart())
async def startBot(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS_IDS:
        await state.set_state(CreatePosts.CreateP)
        await message.answer("👋 Привет, ты находишься в боте для создания и редактирования постов для Telegram-канала"
        "\n\n🔩 Бот находится в разработке, так что при обнаружении багов или ошибок сообщи мне @kirill_r24"
        "\n\n Бот не умее работать с видио и с несколькими медиа, так что в посте должно быть одно фото"
        reply_markup=create_post_keyb)
    else:
        await message.answer("Ты не админ")

@router_start.message(Command("reset"))
async def ressetBot(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS_IDS:
        await state.clear()
        await message.answer("Состояние сброшено.")
    else:
        await message.answer("Ты не админ")
