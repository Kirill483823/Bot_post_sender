from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

draft_post = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📃 Черновик", callback_data="draft_post")]
])
