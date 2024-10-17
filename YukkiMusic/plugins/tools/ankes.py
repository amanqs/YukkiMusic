from pyrogram import filters

from YukkiMusic import app
from YukkiMusic.utils import (antigcast_off, antigcast_on, is_antigcast_on,
                             prouser)


@app.on_message(filters.command("antigcast") & ~filters.private)
@prouser
# @language
async def anti_anti(_, message):
    if len(message.command) != 2:
        return await message.reply_text("Usage: /antigcast [on|off]")
    status = message.text.split(None, 1)[1].strip()
    status = status.lower()
    chat_id = message.chat.id
    if status == "on":
        if await is_antigcast_on(chat_id):
            await message.reply_text("Anti-Gcast already enable.")
        else:
            await antigcast_on(chat_id)
            await message.reply_text(
                "Enabled Anti-Gcast System. I will Delete Messages from Now on."
            )
    elif status == "off":
        if not await is_antigcast_on(chat_id):
            await message.reply_text("Anti-Gcast already disable.")
        else:
            await antigcast_off(chat_id)
            await message.reply_text(
                "Disabled Anti-Gcast System. I won't Be Deleting Message from Now on."
            )
    else:
        await message.reply_text("Unknown Suffix, Use /antigcast [on|off]")
