from pyrogram import filters
from vikky import assistant
import asyncio

gdel = set()

@assistant.on_message(filters.command("gdel") & filters.me)
async def add(client, message):
    if message.reply_to_message:
        gdel.add(message.reply_to_message.from_user.id)
        await message.reply("Added")

@assistant.on_message(filters.group | filters.private)
async def delete(client, message):
    if message.from_user and message.from_user.id in gdel:
        await asyncio.sleep(2)
        try:
            await message.delete()
        except:
            pass
