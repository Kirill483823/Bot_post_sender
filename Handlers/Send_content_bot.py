from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

send_post_router = Router()

#модуль отвечает за кнопку "Выложить пост"


@send_post_router.callback_query(F.data == "send_post")
async def send_post_in_channel(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    photo_id = data.get("draft_photo")
    text = data.get("draft_text")

    if photo_id:
        await callback.bot.send_photo(
            chat_id="@YablokoSerials",
            photo=photo_id,
            caption=text,
            parse_mode="HTML",
        )

    else:
        await callback.bot.send_message(
            chat_id="@YablokoSerials",
            text=text,
            parse_mode="HTML",
            disable_web_page_preview=True
        )

    await callback.answer("Пост опубликован!")
    await callback.message.delete()
    await callback.message.answer("Пост успешно опубликован!")
    await state.clear()
