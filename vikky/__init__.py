from pyrogram import Client
from config import API_ID, API_HASH, STRING_SESSION, BOT_TOKEN

# 👤 Vikky (userbot)
vikky = Client(
    "vikky_userbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION
)

# 🤖 Bot
bot = Client(
    "vikky_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)
