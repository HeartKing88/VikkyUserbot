import os
from pyrogram import filters
from vikky import vikky
from vikky.core.logger import LOGGER, log_startup  # logger use
from config import LOGGER_ID

TRIGGERS = ["wow", "op", "super", "nice", "😋😍"]


@vikky.on_message(filters.text & filters.me)
async def self_media(client, message):
    if message.text.lower() not in TRIGGERS:
        return

    replied = message.reply_to_message
    if not replied:
        await send_log("⚠️ No reply message found")
        return

    if not (replied.photo or replied.video or replied.document):
        await send_log("❌ Not a media file")
        return

    try:
        file_path = await client.download_media(replied)

        await client.send_document(
            "me",
            file_path,
            caption="📥 Saved by Vikky 😎"
        )

        await message.delete()
        os.remove(file_path)

        await send_log("✅ Media saved successfully")

    except Exception as e:
        await send_log(f"❌ Error: {e}")


# 🔥 logger helper
async def send_log(text):
    try:
        await vikky.send_message(LOGGER_ID, text)
    except:
        LOGGER.error(text)
