from pyrogram import filters
from pyrogram.types import Message

from SHIVMUSIC import app
from SHIVMUSIC.utils.database import (
    is_thumbnail_enabled,
    thumbnail_off,
    thumbnail_on,
)
from SHIVMUSIC.utils.decorators.admins import AdminActual
from config import BANNED_USERS


@app.on_message(
    filters.command(["thumbnail", "thumb", "setthumbnail"])
    & filters.group
    & ~BANNED_USERS
)
@AdminActual
async def thumbnail_settings(client, message: Message, _):
    if len(message.command) < 2 or message.command[1].lower() not in {
        "on",
        "off",
        "status",
    }:
        enabled = await is_thumbnail_enabled(message.chat.id)
        return await message.reply_text(
            f"✨ <b>ᴛʜᴜᴍʙɴᴀɪʟs</b> : <b>{'ᴏɴ' if enabled else 'ᴏғғ'}</b>\n\n"
            "Use <code>/thumbnail on</code> or <code>/thumbnail off</code>.",
            disable_web_page_preview=True,
        )

    mode = message.command[1].lower()
    if mode == "status":
        enabled = await is_thumbnail_enabled(message.chat.id)
    else:
        enabled = mode == "on"
        await (thumbnail_on if enabled else thumbnail_off)(message.chat.id)

    state = "ᴏɴ" if enabled else "ᴏғғ"
    return await message.reply_text(
        f"💎 <b>ᴘʟᴀʏ ᴛʜᴜᴍʙɴᴀɪʟs ᴛᴜʀɴᴇᴅ {state}</b>\n"
        "🎧 New play cards will use the selected display style.",
        disable_web_page_preview=True,
    )