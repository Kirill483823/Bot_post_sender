from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



create_post_keyb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✏️ Создать пост", callback_data="create_post")]
])

sendler = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📤 Выложить пост", callback_data="send_posts")]
])


on_main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="На главную", callback_data="on_main")]
])
