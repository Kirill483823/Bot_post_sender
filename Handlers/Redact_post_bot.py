

from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from States.user_states import CreatePosts
from Keyboards.send_content_keyboard import send_post_keyb


redact_post_router = Router()

auto_podpis1 = '<a href="https://t.me/YablokoPodderjkaBot">📨 Прислать новость</a>'
auto_podpis2 = '<a href="https://t.me/YablokoSerials">Яблоко🍎</a>'

#если пользователь отправит тект и фото или толко фото
@redact_post_router.message(CreatePosts.AwaitPost, F.photo)
async def catch_content(message: Message, state: FSMContext):
    photo = message.photo[-1]
    text = message.caption

    await state.update_data(draft_photo=photo.file_id)

    if text:
        text = f"{text}\n{auto_podpis1}\n{auto_podpis2}"
        await state.update_data(draft_text=text)

        await message.answer_photo(
            photo=photo.file_id,
            caption=text,
            parse_mode="HTML",
            reply_markup=send_post_keyb
        )
    else:
        text = f"{auto_podpis1}\n{auto_podpis2}"
        await state.update_data(draft_text=text)

        await message.answer_photo(
            photo=photo.file_id,
            caption=text,
            parse_mode="HTML",
            reply_markup=send_post_keyb
        )

#если пользователь отправит только текст
@redact_post_router.message(CreatePosts.AwaitPost, F.text)
async def catch_content_only_text(message: Message, state: FSMContext):

    text = f"{message.html_text}\n{auto_podpis1}\n{auto_podpis2}"

    await state.update_data(draft_text=text)

    await message.answer(text, parse_mode="HTML", disable_web_page_preview=True, reply_markup=send_post_keyb)

# Кнопка «Черновик» — показываем сохранённый пост заново
@redact_post_router.callback_query(F.data == "draft_post")
async def edit_post_draft(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    photo = data.get("draft_photo")
    text = data.get("draft_text")

    if not text:
        await callback.answer("Черновик пуст!", show_alert=True)
        return

    await callback.message.delete()

    if photo:
        await callback.message.answer_photo(
            photo=photo,
            caption=text,
            parse_mode="HTML",
            reply_markup=send_post_keyb
        )
    else:
        await callback.message.answer(
            text,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=send_post_keyb
        )

    await callback.answer()
