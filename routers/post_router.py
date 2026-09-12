from aiogram.types import Message, CallbackQuery
from aiogram import Router, F, Bot
from keyboards.kb_main import sendler, on_main_menu

CHANNEL_ID = "@YablokoSerials"

router = Router()

auto_podpis = '<a href="https://t.me/YablokoPodderjkaBot">📨 Прислать новость</a>'
auto_podpis2 = '<a href="https://t.me/YablokoSerials">Яблоко🍎</a>'

@router.message(F.photo & F.caption)
async def creating_txt(message: Message):
    photo_id = message.photo[-1].file_id
    text = message.html_text

    caption_text = f"{text}\n\n{auto_podpis}\n{auto_podpis2}"

    await message.answer_photo(
        photo=photo_id,
        caption=caption_text,
        parse_mode="HTML",
        reply_markup=sendler
    )

@router.callback_query(F.data == "send_posts")
async def sending(callback, bot: Bot):
    photo_id = callback.message.photo[-1].file_id
    caption = callback.message.html_text
    await callback.message.answer("✅Пост опубликован! Жми /start", reply_markup=on_main_menu)

    await callback.answer() # Отправляем пост в целевой канал
    await bot.send_photo(
        chat_id=CHANNEL_ID,
        photo=photo_id,
        caption=caption,
        parse_mode="HTML"
    )
    await callback.message.delete()
