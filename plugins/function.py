import asyncio

from pyrogram import Client, filters
from pyrogram.enums import MessageMediaType
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply


@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def detect_file(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name  
    if file.file_size > 2000 * 1024 * 1024:
         if not premium:
             return await message.reply_text("upgrade to premium to rename file upto 2GB")
    try:
        await message.reply_text(
            text=f"**__please enter new filename__**\n\n**old filename** :- `{filename}`",
	          reply_to_message_id=message.id,  
	          reply_markup=ForceReply(True)
        )       
    except FloodWait as e:
        await asyncio.sleep(e.value)
        await message.reply_text(
             text=f"**__please enter new filename__**\n\n**old filename** :- `{filename}`",
	           reply_to_message_id=message.id,  
	           reply_markup=ForceReply(True)
        )
    except:
        pass

@Client.on_message(filters.private & filters.reply)
async def select_mode(client, message):
    reply_message = message.reply_to_message
    if (reply_message.reply_markup) and isinstance(reply_message.reply_markup, ForceReply):
        new_name = message.text 
        await message.delete() 
        msg = await client.get_messages(message.chat.id, reply_message.id)
        file = msg.reply_to_message
        media = getattr(file, file.media.value)
        if not "." in new_name:
            if "." in media.file_name:
                extn = media.file_name.rsplit('.', 1)[-1]
            else:
                extn = "mkv"
            new_name = new_name + "." + extn
        await reply_message.delete()

        button = [[InlineKeyboardButton("📁 Dᴏᴄᴜᴍᴇɴᴛ",callback_data = "upload_document")]]
        if file.media in [MessageMediaType.VIDEO, MessageMediaType.DOCUMENT]:
            button.append([InlineKeyboardButton("🎥 Vɪᴅᴇᴏ", callback_data = "upload_video")])
        elif file.media == MessageMediaType.AUDIO:
            button.append([InlineKeyboardButton("🎵 Aᴜᴅɪᴏ", callback_data = "upload_audio")])
        await message.reply(
            text=f"**Sᴇʟᴇᴄᴛ Tʜᴇ Oᴜᴛᴩᴜᴛ Fɪʟᴇ Tyᴩᴇ**\n**• Fɪʟᴇ Nᴀᴍᴇ :-**```{new_name}```",
            reply_to_message_id=file.id,
            reply_markup=InlineKeyboardMarkup(button)
        )
