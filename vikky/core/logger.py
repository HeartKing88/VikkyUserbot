import logging
from config import LOGGER_ID
from vikky import assistant, bot

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

LOGGER = logging.getLogger("VikkyUserbot")


async def log_startup():
    try:
        me = await assistant.get_me()
        await assistant.send_message(
            LOGGER_ID,
            f"👤 Userbot Started\nName: {me.first_name}\nID: {me.id}"
        )
    except:
        pass

    try:
        bot_me = await bot.get_me()
        await bot.send_message(
            LOGGER_ID,
            f"🤖 Bot Started\nName: {bot_me.first_name}\nID: {bot_me.id}"
        )
    except:
        pass
