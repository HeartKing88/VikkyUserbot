from pyrogram import filters
from vikky import assistant
import asyncio

approved = set()
warn = {}

@assistant.on_message(filters.private & ~filters.me)
async def pm(client, message):
    user = message.from_user.id

    if user in approved:
        return

    warn[user] = warn.get(user, 0) + 1

    if warn[user] == 1:
        await message.reply("⚠️ Wait for approval")
    elif warn[user] == 2:
        await message.reply("⚠️ Last warning")
    else:
        await message.reply("❌ Blocking...")
        await asyncio.sleep(3)
        await client.block_user(user)
