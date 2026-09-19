from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from States.user_states import CreatePosts
from Keyboards.send_content_keyboard import send_post_keyb


redact_post_router = Router()

auto_podpis=('\n<a href="https://t.me/YablokoPodderjkaBot">📨 Прислать новость</a>\n'
                '<a href="https://t.me/YablokoSerials">Яблоко🍎</a>'
            )

#если пользователь отправит тект и фото или толко фото
@redact_post_router.message(CreatePosts.AwaitPost, F.photo)
async def catch_content(message: Message, state: FSMContext):
    await state.set_state(CreatePosts.AwaitSendPost)
    photo = message.photo[-1]
    before_text = message.html_caption or ""

    text = f"{before_text}{auto_podpis}".strip() #это для удаления лишнего пробела в начале
                                                 #в случае если человек не отправит текст

    await state.update_data(draft_photo=photo.file_id, draft_text=text)

    await message.answer_photo(
        photo = photo.file_id,
        caption = text,
        parse_mode="HTML",
        reply_markup=send_post_keyb
    )

#если пользователь отправит только текст
@redact_post_router.message(CreatePosts.AwaitPost, F.text)
async def catch_content_only_text(message: Message, state: FSMContext):
    await state.set_state(CreatePosts.AwaitSendPost)
    text = f"{message.html_text}{auto_podpis}"
    await state.update_data(draft_text=text)

    # Отправляем просто текст
    await message.answer(
        text,
        parse_mode="HTML",
        disable_web_page_preview=True,
        reply_markup=send_post_keyb
    )

#кнопка черновик
@redact_post_router.callback_query(CreatePosts.AwaitSendPost, F.data == "draft_post")
async def edit_post_draft(callback: CallbackQuery, state: FSMContext):

    await state.set_state(CreatePosts.AwaitSendPost) #ставим в ожидание публикации
                                                     #или редактирования
    data = await state.get_data()
    photo_id = data.get("draft_photo")
    text = data.get("draft_text")

    if photo_id:        #если в черновике есть фото
       await callback.message.answer_photo(
           photo=photo_id,
           caption=text,
           parse_mode="HTML",
           reply_markup=send_post_keyb
       )
    else:
        await callback.message.answer(
            text = text,
            parse_mode="HTML",
            reply_markup=send_post_keyb
        )
    await callback.answer("Черновик открыт!")