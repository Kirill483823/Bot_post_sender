from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from States.user_states import CreatePosts

from Keyboards.Create_keyboards import draft_post


router_create_post = Router()

#нажатие на "создать пост"
@router_create_post.callback_query(F.data == "create_post")
async def create(callback: CallbackQuery, state: FSMContext):
    await state.set_state(CreatePosts.AwaitPost)

    data = await state.get_data()
    draft_text = data.get("draft_text")

    if draft_text:
         await callback.answer("⚠️Внимание! Есть черновик, новый текст полностью перезапишет его!", show_alert=True)
         await callback.message.edit_text("📃Отправь пост (черновик будет перезаписан)", reply_markup=draft_post)

    else:
        await callback.answer()
        await callback.message.edit_text("📃Отправь пост")
