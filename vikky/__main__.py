from vikky import vikky, bot
from vikky.core.logger import LOGGER, log_startup
import config
import os
import asyncio

# start clients
vikky.start()
bot.start()

# set runtime owner
me = vikky.get_me()
config.OWNER_ID = me.id

LOGGER.info(f"👑 Owner: {me.id}")

# load modules
for file in os.listdir("vikky/modules"):
    if file.endswith(".py") and file != "__init__.py":
        __import__(f"vikky.modules.{file[:-3]}")

# load core
import vikky.core.bot
import vikky.core.eval

# startup log (async safe)
loop = asyncio.get_event_loop()
loop.create_task(log_startup())

LOGGER.info("🚀 Vikky System Started")

loop.run_forever()
