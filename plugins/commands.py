from Script import script
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user = message.from_user
    button = InlineKeyboardMarkup([[
        InlineKeyboardButton("Help & Settings", callback_data='help')
        ],[
        InlineKeyboardButton('🎟️ Upgrade', callback_data='upgrade'),
        InlineKeyboardButton('🗣️ More', callback_data='more')
    ]])
    await message.reply_text(text=script.START_TXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)
   
