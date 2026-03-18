from vikky import assistant, bot
from vikky.core.logger import LOGGER, log_startup
import config
import os
import asyncio

assistant.start()
bot.start()

me = assistant.get_me()
config.OWNER_ID = me.id

LOGGER.info(f"Owner: {me.id}")

# modules load
for file in os.listdir("vikky/modules"):
    if file.endswith(".py") and file != "__init__.py":
        __import__(f"vikky.modules.{file[:-3]}")

# core load
import vikky.core.bot
import vikky.core.eval

# startup log
asyncio.get_event_loop().create_task(log_startup())

LOGGER.info("🚀 System Started")

asyncio.get_event_loop().run_forever()
