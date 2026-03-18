from pyrogram import filters
from vikky import vikky
from vikky.utils.filters import owner_or_sudo
import asyncio

approved = set()
warn = {}
last_msg = {}

LIMIT = 3

# 🖼️ apni photo ka link ya file_id daalna
PM_PIC = "https://graph.org/file/your_image.jpg"


# 📝 Message templates
MSG_PERMIT = """
<b>PM_SECURITY VIKKY-USERBOT</b>

{}

━━━━━━━━━━━━━━━━━━━━━━━
⍟ You have <b>{}/{}</b> warning!!!
"""

DEFAULT = """
<b>WELCOME....</b>

Hi, this is the keeper of private messages.  
Don't spam or you'll be blocked.

⏳ Wait until my master receives your message.
"""


# 🔐 PM Permit
@vikky.on_message(filters.private & filters.incoming & ~filters.me)
async def pm_permit(client, message):
    if not message.from_user:
        return

    user = message.from_user

    if user.is_bot or user.is_self or user.is_contact:
        return

    if user.id in approved:
        return

    # warning count
    warn[user.id] = warn.get(user.id, 0) + 1

    # delete old msg
    if user.id in last_msg:
        try:
            await last_msg[user.id].delete()
        except:
            pass

    # spam detect
    if warn[user.id] > LIMIT:
        await message.reply("🚫 Spammer detected! Blocking...")
        await client.block_user(user.id)
        warn[user.id] = 0
        return

    # final text
    text = MSG_PERMIT.format(
        DEFAULT,
        warn[user.id],
        LIMIT
    )

    # 📸 send photo + caption
    msg = await message.reply_photo(
        PM_PIC,
        caption=text,
        parse_mode="html"
    )

    last_msg[user.id] = msg
