from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

send_post_keyb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📤Выложить пост", callback_data="send_post")]
])
