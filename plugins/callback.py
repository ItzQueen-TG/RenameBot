from Script import script
from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    user = query.from_user
    data = query.data 
    if data == "start":
        button = InlineKeyboardMarkup([[
            InlineKeyboardButton("Help & Settings", callback_data='help')
        ],[
            InlineKeyboardButton('🎟️ Upgrade', callback_data='premium'),
            InlineKeyboardButton('🗣️ More', callback_data='more')
        ]])
        await query.message.edit_text(text=script.START_TXT.format(user.mention), disable_web_page_preview=True)
    elif data == "help":
        await query.message.edit_text(text="help {}".format(user.mention), disable_web_page_preview=True)
    elif data == "settings":
        await query.message.edit_text(text="settings {}".format(user.mention), disable_web_page_preview=True)
    elif data == "premium":
        await query.message.edit_text(text="premium {}".format(user.mention), disable_web_page_preview=True)
    elif data == "more":
        await query.message.edit_text(text="more {}".format(user.mention), disable_web_page_preview=True)
