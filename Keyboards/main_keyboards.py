from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

create_post_keyb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✏️ Создать пост", callback_data="create_post")]
])
