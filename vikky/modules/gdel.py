from pyrogram import filters
from vikky import vikky
from vikky.utils.filters import owner_or_sudo
import asyncio

gdel = set()


# ➕ ADD USER
@vikky.on_message(filters.command("gdel", prefixes=[".", "/"]) & owner_or_sudo)
async def add(client, message):
    if not message.reply_to_message:
        return await message.reply("Reply to user")

    user_id = message.reply_to_message.from_user.id
    gdel.add(user_id)

    await message.reply(f"✅ Added to GDEL\n🆔 {user_id}")


# ➖ REMOVE USER
@vikky.on_message(filters.command("ungdel", prefixes=[".", "/"]) & owner_or_sudo)
async def remove(client, message):
    if not message.reply_to_message:
        return await message.reply("Reply to user")

    user_id = message.reply_to_message.from_user.id

    if user_id in gdel:
        gdel.remove(user_id)
        await message.reply(f"❌ Removed from GDEL\n🆔 {user_id}")
    else:
        await message.reply("User not in GDEL list")


# 📋 LIST USERS
@vikky.on_message(filters.command("glist", prefixes=[".", "/"]) & owner_or_sudo)
async def list_users(client, message):
    if not gdel:
        return await message.reply("❌ GDEL list empty")

    text = "📋 <b>GDEL Users:</b>\n\n"
    for user_id in gdel:
        text += f"• <code>{user_id}</code>\n"

    await message.reply(text, parse_mode="html")


# 🗑 AUTO DELETE
@vikky.on_message(filters.group | filters.private)
async def delete(client, message):
    if not message.from_user:
        return

    if message.from_user.id in gdel:
        await asyncio.sleep(2)  # safe delay
        try:
            await message.delete()
        except:
            pass
