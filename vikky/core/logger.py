import logging
from config import LOGGER_ID
from vikky import vikky, bot

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

LOGGER = logging.getLogger("VikkyUserbot")


# 🚀 startup log
async def log_startup():
    try:
        me = await vikky.get_me()
        await vikky.send_message(
            LOGGER_ID,
            f"👤 <b>Userbot Started</b>\n\n"
            f"👤 Name: {me.first_name}\n"
            f"🆔 ID: <code>{me.id}</code>",
            parse_mode="html"
        )
    except Exception as e:
        LOGGER.error(f"Userbot log error: {e}")

    try:
        bot_me = await bot.get_me()
        await bot.send_message(
            LOGGER_ID,
            f"🤖 <b>Bot Started</b>\n\n"
            f"🤖 Name: {bot_me.first_name}\n"
            f"🆔 ID: <code>{bot_me.id}</code>",
            parse_mode="html"
        )
    except Exception as e:
        LOGGER.error(f"Bot log error: {e}")
