from Script import script
from pyrogram import Client
from utils import edit_effect
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
        await edit_effect(query, button)
        await query.message.edit_text(text=script.START_TXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)
    elif data == "help":
        button = InlineKeyboardMarkup([[
            InlineKeyboardButton("Back 🧑‍🦯", callback_data='start')
        ]])
        await edit_effect(query, button)
        await query.message.edit_text(text="help {}".format(user.mention), reply_markup=button, disable_web_page_preview=True)
    elif data == "settings":
        button = InlineKeyboardMarkup([[
            InlineKeyboardButton("Back 🧑‍🦯", callback_data='start')
        ]])
        await edit_effect(query, button)
        await query.message.edit_text(text="settings {}".format(user.mention), reply_markup=button, disable_web_page_preview=True)
    elif data == "premium":
        button = InlineKeyboardMarkup([[
            InlineKeyboardButton("Back 🧑‍🦯", callback_data='start')
        ]])
        await edit_effect(query, button)
        await query.message.edit_text(text="premium {}".format(user.mention), reply_markup=button, disable_web_page_preview=True)
    elif data == "more":
        button = InlineKeyboardMarkup([[
            InlineKeyboardButton("Back 🧑‍🦯", callback_data='start')
        ]])
        await edit_effect(query, button)
        await query.message.edit_text(text="more {}".format(user.mention), reply_markup=button, disable_web_page_preview=True)
