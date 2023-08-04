from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def edit_effect(query, button):
    await query.message.edit_text(
            text="",
            reply_markup=button,
            parse_mode=enums.ParseMode.HTML
    )
