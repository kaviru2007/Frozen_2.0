# Copyright (C) 2023 DX-MODS
#Licensed under the  AGPL-3.0 License;
#you may not use this file except in compliance with the License.
#Author ZIYAN
#if you use our codes try to donate here https://www.buymeacoffee.com/ziyankp

import pyrogram
import asyncio
import os
from pyrogram import filters, Client
from info import PREFIX

@Client.on_message((filters.command(["report"], PREFIX) | filters.regex("@admins") | filters.regex("@admin")) & filters.group)
async def report_user(bot, message):
    if message.reply_to_message:
        chat_id = message.chat.id
        reporter = str(message.from_user.id)
        mention = message.from_user.mention
        admins = await bot.get_chat_members(chat_id=chat_id, filter="administrators")
        success = True
        report = f"𝖱𝖾𝗉𝗈𝗋𝗍𝖾𝗋 : {mention} ({reporter})" + "\n"
        report += f"𝖬𝖾𝗌𝗌𝖺𝗀𝖾 : {message.reply_to_message.link}"
        for admin in admins:
            try:
                reported_post = await message.reply_to_message.forward(admin.user.id)
                await reported_post.reply_text(
                    text=report,
                    chat_id=admin.user.id,
                    disable_web_page_preview=True
                )
                success = True
            except:
                pass
        if success:
            await message.reply_text("𝖱𝖾𝗉𝗈𝗋𝗍𝖾𝖽 𝗍𝗈 𝖠𝖽𝗆𝗂𝗇𝗌!")
