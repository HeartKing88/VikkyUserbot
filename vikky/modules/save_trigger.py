from pyrogram import filters
from vikky import assistant

@assistant.on_message(filters.text & filters.me)
async def save(client, message):
    if message.text.lower() != "wow":
        return

    if not message.reply_to_message:
        return

    msg = message.reply_to_message

    if msg.photo or msg.video or msg.document:
        await msg.copy("me")
        await message.delete()
